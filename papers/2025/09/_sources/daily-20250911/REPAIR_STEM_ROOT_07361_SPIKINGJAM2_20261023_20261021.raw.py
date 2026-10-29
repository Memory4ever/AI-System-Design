import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoTokenizer
import torch.optim as optim
import torch.multiprocessing as mp
from functools import partial
import os
import snntorch as snn
from snntorch import surrogate
import transformers
import pickle
import zipfile
from datasets import load_dataset
from torch.utils.data import DataLoader, IterableDataset
import math
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

transformers.logging.set_verbosity_error()

os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = 'true'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Global parameters
PARAMS = {
    'model_name': 'bert-base-uncased',
    'num_neurons_per_dim': 4,
    'embedding_dim': 300,
    'num_layers': 6,
    'num_heads': 4,
    'max_seq_length': 1024,
    'chunk_size': 512,
    'overlap': 256,
    'fasttext_zip_file': 'wiki-news-300d-1M-subword.vec.zip',
    'batch_size': 8,
    'learning_rate': 1e-4,
    'num_epochs': 10,
    'device': torch.device("cuda" if torch.cuda.is_available() else "cpu"),
    'num_training_samples': 1000,  # Add this line
    'lif_decay_rate': 0.5
}

class StreamingDataset(IterableDataset):
    def __init__(self, dataset, tokenizer, max_length):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __iter__(self):
        for example in self.dataset:
            yield self.tokenizer(example['text'], truncation=True, max_length=self.max_length, return_tensors="pt", padding="max_length")

class SpikeEncoder:
    def __init__(self, params):
        self.device = params['device']
        self.tokenizer = AutoTokenizer.from_pretrained(params['model_name'])
        self.embeddings = self.load_or_create_fasttext_embeddings(params['fasttext_zip_file'])
        self.num_neurons_per_dim = params['num_neurons_per_dim']
        self.max_rate = 1000  # Consider adding this to PARAMS if it needs to be adjustable
    

    def load_or_create_fasttext_embeddings(self, fasttext_zip_file):
        # Define a path for the saved embeddings
        saved_embeddings_path = fasttext_zip_file.replace('.zip', '.pkl')

        # Check if the saved embeddings file exists
        if os.path.exists(saved_embeddings_path):
            print("Loading saved FastText embeddings...")
            with open(saved_embeddings_path, 'rb') as f:
                return pickle.load(f)
        else:
            print("Creating FastText embeddings from zip file...")
            embeddings = self.load_fasttext_embeddings(fasttext_zip_file)
            
            # Save the embeddings
            print("Saving FastText embeddings for future use...")
            with open(saved_embeddings_path, 'wb') as f:
                pickle.dump(embeddings, f)
            
            return embeddings

    def load_fasttext_embeddings(self, fasttext_zip_file):
        embeddings = {}
        with zipfile.ZipFile(fasttext_zip_file, 'r') as zip_ref:
            # Assuming the .vec file has the same name as the .zip file
            vec_filename = os.path.basename(fasttext_zip_file).replace('.zip', '')
            with zip_ref.open(vec_filename) as f:
                # Skip the first line (contains vocab size and dimension)
                next(f)
                for line in f:
                    line = line.decode('utf-8').strip().split()
                    word = line[0]
                    vector = torch.tensor([float(x) for x in line[1:]], device=self.device)
                    embeddings[word] = vector
        return embeddings

    def encode(self, texts, time_steps=100, max_length=None):
        max_length = max_length or PARAMS['max_seq_length']
        # Tokenize input texts
        batch_tokens = [self.tokenizer.tokenize(text)[:max_length] for text in texts]
        
        # Get FastText embeddings for tokens
        embeddings = []
        max_seq_len = max(len(tokens) for tokens in batch_tokens)
        for tokens in batch_tokens:
            token_embeddings = []
            for token in tokens:
                if token in self.embeddings:
                    token_embeddings.append(self.embeddings[token])
                else:
                    # Use a random vector for unknown tokens
                    token_embeddings.append(torch.randn(300, device=self.device))
            # Pad sequences to max_seq_len
            while len(token_embeddings) < max_seq_len:
                token_embeddings.append(torch.zeros(300, device=self.device))
            embeddings.append(torch.stack(token_embeddings))
        
        # Stack embeddings to create a batch
        embeddings = torch.stack(embeddings)
        
        # Generate population code
        spike_trains = self.generate_population_code(embeddings, time_steps)
        return spike_trains

    def generate_population_code(self, embeddings, time_steps):
        batch_size, seq_len, embedding_dim = embeddings.shape
        
        # Normalize embeddings to [0, 1]
        norm_embeddings = (F.normalize(embeddings, p=2, dim=-1) + 1) / 2
        
        # Create preferred values for each neuron in the population
        preferred_values = torch.linspace(0, 1, self.num_neurons_per_dim, device=self.device)
        preferred_values = preferred_values.unsqueeze(0).unsqueeze(0).unsqueeze(0).expand(batch_size, seq_len, embedding_dim, -1)
        
        # Calculate firing rates based on distance to preferred values
        distances = (norm_embeddings.unsqueeze(-1) - preferred_values).pow(2)
        firing_rates = self.max_rate * torch.exp(-distances / 0.1)
        
        # Incorporate temporal positional encoding
        position_offset = torch.arange(seq_len, device=self.device).unsqueeze(0).unsqueeze(-1).unsqueeze(-1).float() / seq_len
        firing_rates = firing_rates * (1 - position_offset.expand(batch_size, -1, embedding_dim, self.num_neurons_per_dim))
        
        spikes = torch.rand_like(firing_rates.unsqueeze(-1).expand(-1, -1, -1, -1, time_steps), device=self.device) < (firing_rates.unsqueeze(-1) / self.max_rate)
        return spikes.float()

class SpikeDecoder:
    def __init__(self, params):
        self.tokenizer = AutoTokenizer.from_pretrained(params['model_name'])
        self.num_neurons_per_dim = params['num_neurons_per_dim']
        self.embedding_dim = params['embedding_dim']
        self.vocab_size = len(self.tokenizer.vocab)
        self.output_layer = nn.Linear(self.num_neurons_per_dim, self.vocab_size).to(params['device'])

    def decode(self, spike_trains):
        # spike_trains shape: [batch_size, seq_len, embedding_dim, num_neurons_per_dim, time_steps]
        batch_size, seq_len, embedding_dim, num_neurons_per_dim, time_steps = spike_trains.shape
        
        # Aggregate spikes over time
        aggregated_spikes = spike_trains.sum(dim=-1)  # [batch_size, seq_len, embedding_dim, num_neurons_per_dim]
        
        # Reshape for linear layer
        reshaped_spikes = aggregated_spikes.permute(0, 1, 3, 2).contiguous()  # [batch_size, seq_len, num_neurons_per_dim, embedding_dim]
        reshaped_spikes = reshaped_spikes.view(batch_size * seq_len * embedding_dim, num_neurons_per_dim)
        
        # Generate logits
        logits = self.output_layer(reshaped_spikes)  # [batch_size * seq_len * embedding_dim, vocab_size]
        logits = logits.view(batch_size, seq_len, embedding_dim, self.vocab_size)
        
        # Average logits across embedding dimension
        averaged_logits = logits.mean(dim=2)  # [batch_size, seq_len, vocab_size]
        
        return averaged_logits

    def decode_to_text(self, logits):
        # Get most likely tokens
        token_ids = logits.argmax(dim=-1)
        
        # Convert token IDs to text
        decoded_tokens = self.tokenizer.convert_ids_to_tokens(token_ids)
        reconstructed_text = self.tokenizer.convert_tokens_to_string(decoded_tokens)
        
        return reconstructed_text

class SpikingLinearLayer(nn.Module):
    def __init__(self, in_features, out_features, params, beta=0.9):
        super().__init__()
        self.fc = nn.Linear(in_features, out_features, bias=False).to(params['device'])
        spike_grad = surrogate.fast_sigmoid()
        self.lif = snn.Leaky(beta=beta, spike_grad=spike_grad)
        self.decay_rate = params['lif_decay_rate']
        self.mem = None
        self.out_features = out_features

    def forward(self, x):
        # x: [batch_size, seq_len, embedding_dim, flattened_dim]
        batch_size, seq_len, embedding_dim, flattened_dim = x.shape

        # Reshape x for processing
        x = x.permute(0, 1, 3, 2).contiguous()  # [batch_size, seq_len, flattened_dim, embedding_dim]
        x = x.view(-1, embedding_dim)  # [batch_size * seq_len * flattened_dim, embedding_dim]

        # Process through linear layer
        syn = self.fc(x)  # [batch_size * seq_len * flattened_dim, out_features]

        # Reshape for LIF neuron processing
        syn = syn.view(batch_size, seq_len, flattened_dim, self.out_features)  # [batch_size, seq_len, flattened_dim, out_features]

        # Apply decay to membrane potential and detach
        if self.mem is None:
            self.mem = torch.zeros_like(syn)
        self.mem = self.mem.detach() * self.decay_rate
        spk, self.mem = self.lif(syn, self.mem)

        # Reshape output to match input shape
        output = spk.permute(0, 1, 3, 2)  # [batch_size, seq_len, out_features, flattened_dim]

        return output

    def reset_state(self):
        self.mem = None

class PhaseShiftedSpikingSelfAttention(nn.Module):
    def __init__(self, params):
        super().__init__()
        self.num_heads = params['num_heads']
        self.head_dim = params['embedding_dim'] // self.num_heads
        self.num_neurons_per_dim = params['num_neurons_per_dim']
        self.embedding_dim = params['embedding_dim']

        self.q_layer = SpikingLinearLayer(params['embedding_dim'], params['embedding_dim'], params)
        self.k_layer = SpikingLinearLayer(params['embedding_dim'], params['embedding_dim'], params)
        self.v_layer = SpikingLinearLayer(params['embedding_dim'], params['embedding_dim'], params)
        self.out_layer = SpikingLinearLayer(params['embedding_dim'], params['embedding_dim'], params)

    def forward(self, x):
        # x: [batch_size, seq_len, embedding_dim, flattened_dim]
        batch_size, seq_len, embedding_dim, flattened_dim = x.shape

        # Compute queries, keys, and values
        q = self.q_layer(x)
        k = self.k_layer(x)
        v = self.v_layer(x)

        # Reshape for attention computation
        q = q.view(batch_size, seq_len, self.num_heads, self.head_dim, flattened_dim)
        k = k.view(batch_size, seq_len, self.num_heads, self.head_dim, flattened_dim)
        v = v.view(batch_size, seq_len, self.num_heads, self.head_dim, flattened_dim)

        # Compute attention scores
        attention_scores = self.compute_attention_scores(q, k)

        # Apply attention weights
        attended_values = self.apply_attention_weights(attention_scores, v)

        # Reshape back to original dimensions
        attended_values = attended_values.contiguous().view(batch_size, seq_len, embedding_dim, flattened_dim)

        # Output projection
        output = self.out_layer(attended_values)

        return output

    def compute_attention_scores(self, q, k):
        return torch.einsum('bqhdf,bkhdf->bqhk', q, k)

    def apply_attention_weights(self, attention_weights, v):
        return torch.einsum('bqhk,bkhdf->bqhdf', attention_weights, v)

    def reset_states(self):
        self.q_layer.reset_state()
        self.k_layer.reset_state()
        self.v_layer.reset_state()
        self.out_layer.reset_state()

class SpikingFeedForward(nn.Module):
    def __init__(self, params):
        super().__init__()
        self.layer1 = SpikingLinearLayer(params['embedding_dim'], 4 * params['embedding_dim'], params)
        self.layer2 = SpikingLinearLayer(4 * params['embedding_dim'], params['embedding_dim'], params)
        spike_grad = surrogate.fast_sigmoid()
        self.lif = snn.Leaky(beta=0.9, spike_grad=spike_grad)
        self.num_neurons_per_dim = params['num_neurons_per_dim']
        self.mem = None

    def forward(self, x):
        x = self.layer1(x)
        if self.mem is None:
            self.mem = torch.zeros_like(x)
        spk, self.mem = self.lif(x, self.mem)  # Use LIF with membrane potential
        x = self.layer2(spk)
        return x

    def reset_states(self):
        self.layer1.reset_state()
        self.layer2.reset_state()
        self.mem = None

class CustomLayerNorm(nn.Module):
    def __init__(self, normalized_shape):
        super().__init__()
        self.layer_norm = nn.LayerNorm(normalized_shape)

    def forward(self, x):
        # x: [batch_size, seq_len, embedding_dim, flattened_dim]
        orig_shape = x.shape
        x = x.view(-1, x.size(-2), x.size(-1))
        x = self.layer_norm(x.transpose(1, 2)).transpose(1, 2)
        return x.view(orig_shape)

class SpikingTransformerLayer(nn.Module):
    def __init__(self, params):
        super().__init__()
        self.self_attention = PhaseShiftedSpikingSelfAttention(params)
        self.feedforward = SpikingFeedForward(params)
        self.layer_norm1 = CustomLayerNorm(params['embedding_dim'])
        self.layer_norm2 = CustomLayerNorm(params['embedding_dim'])

    def forward(self, x):
        attended = self.self_attention(x)
        x = self.layer_norm1(x + attended)
        ff_output = self.feedforward(x)
        x = self.layer_norm2(x + ff_output)
        return x

    def reset_states(self):
        self.self_attention.reset_states()
        self.feedforward.reset_states()

class SpikingTransformer(nn.Module):
    def __init__(self, params):
        super().__init__()
        self.layers = nn.ModuleList([SpikingTransformerLayer(params) for _ in range(params['num_layers'])])

    def forward(self, x):
        # x: [batch_size, seq_len, embedding_dim, num_neurons_per_dim, time_steps]
        batch_size, seq_len, embedding_dim, num_neurons_per_dim, time_steps = x.shape
        
        # Reshape to combine num_neurons_per_dim and time_steps
        x = x.view(batch_size, seq_len, embedding_dim, -1)
        
        for layer in self.layers:
            x = layer(x)
        
        # Reshape back to original dimensions
        x = x.view(batch_size, seq_len, embedding_dim, num_neurons_per_dim, time_steps)
        
        return x

    def reset_states(self):
        for layer in self.layers:
            layer.reset_states()

class SpikingTransformerModel(nn.Module):
    def __init__(self, params):
        super().__init__()
        self.encoder = SpikeEncoder(params)
        self.transformer = SpikingTransformer(params)
        self.decoder = SpikeDecoder(params)
        self.max_seq_length = params['max_seq_length']
        self.device = params['device']

    def forward(self, batch_texts):
        self.reset_states()
        spike_trains = self.encoder.encode(batch_texts, max_length=self.max_seq_length).to(self.device)
        spike_trains_with_pos = self.add_positional_encoding(spike_trains)
        transformed_spike_trains = self.transformer(spike_trains_with_pos)
        logits = self.decoder.decode(transformed_spike_trains)
        return logits

    def generate(self, input_text, max_length=100):
        spike_trains = self.encoder.encode(input_text).to(self.device)
        generated = []
        for _ in range(max_length):
            spike_trains_with_pos = self.add_positional_encoding(spike_trains)
            transformed = self.transformer(spike_trains_with_pos)
            logits = self.decoder.decode(transformed)
            next_token = logits[:, -1, :].argmax(dim=-1)
            generated.append(next_token.item())
            if next_token.item() == self.encoder.tokenizer.eos_token_id:
                break
            new_spike = self.encoder.encode(self.encoder.tokenizer.decode([next_token.item()])).to(self.device)
            spike_trains = torch.cat([spike_trains, new_spike], dim=0)
        return self.encoder.tokenizer.decode(generated)

    def process_chunk(self, chunk):
        return self.transformer(chunk)

    def add_positional_encoding(self, spike_trains):
        batch_size, seq_len, embedding_dim, num_neurons, time_steps = spike_trains.shape
        position = torch.arange(seq_len, device=spike_trains.device).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, embedding_dim, 2, device=spike_trains.device) * -(math.log(10000.0) / embedding_dim))
        pos_encoding = torch.zeros(seq_len, embedding_dim, device=spike_trains.device)
        pos_encoding[:, 0::2] = torch.sin(position * div_term)
        pos_encoding[:, 1::2] = torch.cos(position * div_term)
        
        # Add positional encoding to the spike rates
        spike_rates = spike_trains.sum(dim=-1) / time_steps  # Average spike rate
        encoded_rates = spike_rates + pos_encoding.unsqueeze(0).unsqueeze(-1) * 0.1  # Scale factor to balance with spike information
        
        # Convert back to spike trains
        encoded_spike_trains = (encoded_rates.unsqueeze(-1) > torch.rand_like(spike_trains)).float()
        
        return encoded_spike_trains

    def reset_states(self):
        self.transformer.reset_states()
        # Reset encoder and decoder states if they have any
        if hasattr(self.encoder, 'reset_states'):
            self.encoder.reset_states()
        if hasattr(self.decoder, 'reset_states'):
            self.decoder.reset_states()

    # Remove or comment out the clear_graph method if not used elsewhere
    # def clear_graph(self):
    #     for param in self.parameters():
    #         if param.grad is not None:
    #             param.grad.detach_()
    #             param.grad.zero_()

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group("nccl", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

def train(rank, world_size, params):
    setup(rank, world_size)
    
    params['device'] = torch.device(f"cuda:{rank}")
    model = SpikingTransformerModel(params).to(params['device'])
    model = DDP(model, device_ids=[rank])
    
    dataset = load_dataset("bookcorpus", streaming=True)
    tokenizer = AutoTokenizer.from_pretrained(params['model_name'], trust_remote_code=True)
    streaming_dataset = StreamingDataset(dataset['train'], tokenizer, params['max_seq_length'])
    
    sampler = DistributedSampler(streaming_dataset, num_replicas=world_size, rank=rank, shuffle=True)
    train_dataloader = DataLoader(streaming_dataset, batch_size=params['batch_size'], sampler=sampler, num_workers=1)
    
    train_model(model, train_dataloader, params, rank)
    
    cleanup()

def train_model(model, train_dataloader, params, rank):
    model.train()
    optimizer = optim.Adam(model.parameters(), lr=params['learning_rate'])
    loss_fn = nn.CrossEntropyLoss(ignore_index=0)

    for epoch in range(params['num_epochs']):
        train_dataloader.sampler.set_epoch(epoch)
        total_loss = 0
        for i, batch in enumerate(train_dataloader):
            if i >= params['num_training_samples'] // (params['batch_size'] * torch.cuda.device_count()):
                break
            
            optimizer.zero_grad()
            model.module.reset_states()  # Reset states at the beginning of each batch
            
            input_ids = batch['input_ids'].squeeze(1).to(params['device'])
            
            batch_texts = []
            for seq in input_ids:
                text = model.module.encoder.tokenizer.decode(seq, skip_special_tokens=True)
                batch_texts.append(text)
            
            try:
                logits = model(batch_texts)
                
                if rank == 0:
                    print(f"Batch {i}: Input shape: {input_ids.shape}, Output shape: {logits.shape}")
                
                target = F.pad(input_ids, (0, logits.size(1) - input_ids.size(1)))
                
                loss = loss_fn(logits.view(-1, logits.size(-1)), target.view(-1))
                
                loss.backward()
                
                # Clip gradients
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                
                optimizer.step()
                
                total_loss += loss.item()
                
                if rank == 0:
                    print(f"Batch {i}: Loss: {loss.item()}")
                
            except RuntimeError as e:
                print(f"Error in batch {i}: {str(e)}")
                raise e
            
            # Ensure we're not retaining the graph
            del logits, loss
            torch.cuda.empty_cache()
        
        if rank == 0:
            print(f"Epoch {epoch+1}/{params['num_epochs']}, Avg Loss: {total_loss / (i+1)}")

if __name__ == "__main__":
    world_size = torch.cuda.device_count()
    mp.spawn(train, args=(world_size, PARAMS), nprocs=world_size, join=True)