# CLEAR

Dissecting Transformers.

Here, we provide the artifact for measuring component-wise energy in a transformer.

```store_activations.py``` is used to Cache the activations of the transformer for an inference, for faster usage later on

```module_measure.py``` is used to measure the energy of components such as Attention, MLP, Embedding etc in a layer

```layer_measure.py``` is used to calculate energy across a layer

Note that this methodology is a proof of concept which can be generalized to differences in transformer architecture, the core idea remaining the same. For different families of transformer, the code may need changes to accomodate different internal architecture. For this repository, we provide example on the BERT transformer.