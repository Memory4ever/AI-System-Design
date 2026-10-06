[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] p: hoefler-corrected-gossipCorrected Gossip

[3] h1: Fault-tolerant Reduce and Allreduce operations based on correction

[4] h2: 1 Introduction

[5] p: When multiple processes, i.e. independently executing entities, potentially executing on distinct hardware, collaborate to achieve a common goal they require communication. One prominent example of this scenario is HPC .

[6] p: Beyond one to one communication (also called Point-to-Point-communication ), that only involves two communication partners, important operations to facilitate this communication are so called collective (communication) operations , where a potentially bigger set of processes exchanges data following some communication pattern [ 1 ] .

[7] p: Commonly used examples of such communication patterns are broadcast, where one process sends the same data to all other participants, reduce, where all processes contribute some data and one process receives the combined result, and allreduce, which works like reduce but all processes receive the result. These operations are examples for the more general communication patterns one to many, many to one, and many to many.

[8] p: It is common to replace ‘many’ with ‘all.’ Usually a different technique is used for restricting the set of processes participating, e.g., MPI groups 1 1 1 A MPI communicator, that is directly used to achieve this, uses a MPI group to store membership. [ 2 ] . This point of view is adopted in this document: It is always assumed that all processes take part in the collective communication operations.

[9] p: Point-to-point messages are a primitive operation of computer networks. Collective operations can be implemented using that primitive, i.e., by sending multiple one to one messages between selected processes. The goal of this document are algorithms that implement a collective operation using this primitive.

[10] p: For example, broadcast can be implemented by sending messages along the edges of a tree that is rooted at the original sender of the broadcast (the root process). Processes correspond to vertices in the tree, and each process sends the data to all its children, after receiving the data (if the vertex has a parent in the tree).

[11] p: This example shows how process failures, where a process fails to send some or all messages pertaining to the collective algorithm, impede the collective operation. If in the tree one process does not send messages to the processes corresponding to its child vertices, all subtrees rooted at its children do not receive any data.

[12] p: The focus of this work are fault tolerant algorithms for reduce and allreduce operations with small messages. Failures of communicating processes are considered exclusively, in contrast to missing/delayed/otherwise impeded messages.

[13] p: Algorithms for reduce, and allreduce are presented in this paper. An algorithm for broadcast was previously described [ 6 ] .

[14] p: The semantics of fault tolerance aimed for in this paper is: If not more than a number f f of processes fail preoperationally (i.e. before the communication operation), the collective operation provides the same result as if the failed processes were excluded by all participating processes in advance. Processes failing inoperationally (during the operation) can appear either alive or dead with respect to the operation, but no mixed state is allowed.

[15] p: The algorithms target small messages. For big messages, they still behave correctly, but other implementations are more efficient. Which sizes constitute a small or big message cannot be stated in general, and is not discussed here. A rough distinction can be made based on whether the operation is latency critical (the focus of this work), or bandwidth critical.

[16] h2: 2 Related work

[17] p: Correction was first used by [ 4 ] [ 4 ] in combination with an unreliable hardware multicast. It was intended to be executed after a hardware multicast, to correct for potential omissions, in order to turn the operation into a broadcast. However, only probabilistic guarantees are given.

[18] p: The basic purpose of up-correction is the same: to correct omissions made by the fault-agnostic algorithm of reduce. It the context of this work, omissions are not random, but deterministically caused by process failures.

[19] p: The idea of correction was significantly expanded upon by [ 3 ] [ 3 ] in the work on \citetalias hoefler-corrected-gossip. Three different correction algorithms with different semantics are proposed. They are all intended to be combined with a gossip phase that disseminates a broadcast value probabilisticly. Following this step, correction is used to improve the probabilities provided by gossip, or for some correction algorithms even give some guarantees, under assumptions on the number and timing of process failures.

[20] p: The up-correction algorithm described in Section 4.2 are based the same ideas as the correction algorithms used in \citetalias hoefler-corrected-gossip. They serve a different purpose, however. In \citetalias hoefler-corrected-gossip the correction algorithms are used to help against the inherent shortcoming of gossip, i.e., that messages are sent randomly and thus some processes might never receive a message. Their use has no relation to fault tolerance there. Instead, disseminating information by sending messages to random participants is inherently tolerant to crash process failures. In this document, the up-correction algorithm are used to correct omissions induced by process failures.

[21] p: In addition to the theoretical difference of the purpose of correction, there is a practical difference between \citetalias hoefler-corrected-gossip’s correction and up-correction as used in this work. In \citetalias hoefler-corrected-gossip, the gossip phase, and the following correction phase are assumed to be two globally separate phases. The published algorithm is only simulated, not practically implemented. Conversely, in this work the active phase is a local, not a global, property: processes execute the phases in succession, but independently of the progress of other processes.

[22] h2: 3 Failures

[23] p: In this document failures of processes are assumed to follow a fail-stop -model, i.e., processes that fail stop sending any messages. Sending to a failed process does not provide any indication of the failure. Instead, the send operation completes like a send operation to a live process, and the failed process will not provide any reaction to the message. This is also sometimes called a crash failure model. Distinctions between the two terms are made inconsistently, and none are assumed here.

[24] p: The network is assumed to be reliable, i.e., messages are not lost, reordered, or modified. In other words, no communication failures are possible.

[25] h2: 4 Reduce

[26] p: Without loss of generality it is assumed that the recepient of the reduce (i.e., the root) is process 0 0 . If this is not the case, its number can be swaped with that of process 0 0 to restore this property.

[27] p: The basic reduction function is assumed to be assocative (as, e.g., mandated by MPI [ 2 ] ) and commutative for the description below.

[28] p: The following terminology is used. A reduce operation is identified by a reduce message m m . The contents of this message are defined below. Processes do not need to receive a message before sending one. Depending on the implementation, some processes need to receive a message first, but logically most processes just contribute a value, and do not receive any information. Thus, reduce messages for the same operation are created by multiple processes.

[29] p: Before sending any network messages related to m m , a process indicates its intention by calling init_reduce( m m ) . After the reduce-operation is completed locally, i.e., for a non-root process after sending all information to the parent process, and for the root after the final result is available the process reports to the caller by calling deliver_reduce( m m ) .

[30] p: A reduce message has the following data members:

[31] p: (A descriptor of) the set of participating processes.

[32] p: A unique id.

[33] h3: 4.1 Semantics

[34] p: Let n n processes execute reduce. Up to f f arbitrary processes may fail either pre-operationally or in-operationally.

[35] p: If the root calls deliver_reduce( m m ) , all non-failed processes have called init_reduce( m m ) .

[36] p: Each process calls deliver_reduce( m m ) at most once for a given m m .

[37] p: The value returned by reduce at a non-failed root includes the input values of all non-failed processes.

[38] p: Values of failed processes are either included normally, or disregarded. No intermediate stages are possible.

[39] p: Each non-failed process executes deliver_reduce( m m ) eventually, if all non-failed processes execute init_reduce( m m ) .

[40] p: Reduce sent to a failed process simply becomes a no-op.

[41] h3: 4.2 Up-Correction

[42] p: The underlying idea of the algorithm for reduce presented in this document is to combine a tree phase with a preceeding up-correction phase. The tree phase implements the reduce operation completely in the failure-free case.

[43] p: In case a process fails, the dissimination of data is inhibited. The tree phase consists of every process receiving messages all children, followed by every process except the root sending a single messages to its parent in the tree. This dissimination of data is inhibited in case there is a faulty procss that does not send a message to its parent.

[44] figure: Input: The data contributed by this process Output: The data used in the tree phase by all processes in this up-correction group function up_correction( data ) begin group ← \leftarrow compute_up_correction_group(f, process_id ) senddata ← \leftarrow data for p ∈ p\in group ∖ { process_id } \setminus\{\textnormal{{process\_id}}\} do Note: no failure information is sent here send (senddata) to p p receive (data) from p p data ← \leftarrow reduce_function( data , received data) end for return data end Algorithm 1 Up-correction

[45] p: To compensate for this problem, processes exchange their data in up-correction groups in the up-correction phase prior to the tree phase.

[46] p: To tolerate up to f f failures, all processes p p that share the group number ⌊ p − 1 f + 1 ⌋ \left\lfloor\frac{p-1}{f+1}\right\rfloor form one up-correction group and exchange messages. In addition, if the last group (the one with the highest number) has less than f + 1 f+1 members, the root is also part of it. Otherwise, the root does not belong to any group. Values are exchanged with (sent to, and received from) each other member in the same group.

[47] p: Values are exchanged in the group, and reduced, i.e., combined using the reduction function, locally. The result is that all members of an replication group have the same value after their up-correction phase (in-operation make this situation more complicated. If members of a group experience in-operation, the final value of other members of the group might or might not include the value of the failed process. Both results are considered correct in the semantics of reduce. This value is used in the tree phase. Details are in the description of reduce, see Section 4.3 .

[48] p: The motivation of the design of the groups is that processes with the same number in the subtrees of the root exchange values. This limits the number of messages that are sent and received by each process, and enables the root to efficiently reason about which value is included in which subtree.

[49] p: Note that in an up-correction group that includes at least one failed process, all live processes will time out on the respective receive operations and will confirm the sender to have failed with the respective failure monitor. The resulting delay is unfortunate, but not avoidable: In reduce, where every process contributes a value, each process that fails to send a value must be confirmed to have failed. How this is done is independent of the communication algorithm. Timeouts are used here.

[50] h3: 4.3 Algorithm

[51] figure: Input: The data contributed by this process Output: The resulting data function reduce_root( data ) begin if root is in a up-correction group then data ← \leftarrow up_correction ( data ) end if msg, c c ← \leftarrow receive from any child c c (data, failure information) if failure information indicates failure in subtree then continue end if if root data not included in data from sender (determined from sender id) then return basic_reduce_function( data , received data) else return received data end if raise Error(“No failure-free subtree”) end Algorithm 2 Fault tolerant reduce, algorithm executed at the root

[52] figure: Input: The data contributed by this process function reduce_non_root( data ) begin data ← \leftarrow up_correction ( data ) for c ∈ c\in children do receive (data, failure information) from c c data ← \leftarrow basic_reduce_function( data , received data) update failure information end for send ( data , failure information) to parent end Algorithm 3 Fault tolerant reduce, algorithm executed at non-roots

[53] figure: Input: The data contributed by this process, and the number of the root process Output: At the root: The resulting data function reduce( data , root ) begin if process_id == root then return reduce_root( data ) else reduce_non_root( data ) end if end Algorithm 4 Fault tolerant reduce, that calls either version above

[54] p: Processes that fail before calling a reduce operation do not contribute their input value. This can not be avoided. The purpose of this fault tolerant operation is to make sure that these processes do not hinder other processes from contributing their input value.

[55] p: For the sake of the description, it is assumed that the root process does not fail. No workaround for the case of a failed root is necessary. If the root fails (pre-operational or in-operational), this operation becomes a no-op, adhering to the semantics.

[56] p: Processes first execute the up-correction algorithm, and then execute a tree phase, in which a normal reduce up a tree is performed.

[57] p: The up-correction phase is described in Section 4.2 . The resulting reduced value is then used in the tree phase to be delivered to the parent process.

[58] p: In the failure-free case, the root process gets values from all its children that in total (including the value of the root itself) include each value f + 1 f+1 times. By selecting one value it received, the root gets the correct value. Which value the root should select, based on the information on failures, is explained in Section 4.4 . There are multiple ways for failure information to be propagated.

[59] figure: 0 1 2 3 4 5 6 1 4–6 2 3 5 6 Figure 1: The failed process 1 impedes the propagation of data in the tree phase. Arrow labels show the values of which processes are included in the respective message along the path.

[60] figure: 0 1 3 5 2 4 6 1 2–6 3,4 5,6 3,4 5,6 Figure 2: Up-correction phase and subsequent tree phase with the same failed processes as in Figure 1 .

[61] p: As an example of reduce with a failed processes, consider seven processes that want to compute the sum of their process numbers, or rank numbers in MPI terms. The process number is a unique identifier in the range 0 0 to 6 6 . Process 1 1 is assumed to have failed. The goal is thus to compute the sum of the remaining process numbers 0 + 2 + 3 + 4 + 5 + 6 = 20 0+2+3+4+5+6=20 . Process 0 0 is the root of the reduce operation. Figures 1 and 2 depict the communication sent in this scenario in a “common” tree implementation, and in the tree phase of the algorithm presented here. The algorithm constitutes an up-correction phase and a tree phase. The labels of the arrows in Figures 1 and 2 depict the process ids whose values are included in the (partial) sum sent in the respective message (this information is not sent, and is only included in the picture for illustrative purpose). Since each process sends its process id as a value in this example, the sum of the numbers listed is the value being sent in each message.

[62] p: In the tree algorithm, which corresponds to the tree phase, the processes at the leaf positions in the tree start by sending their process number to their parents. I.e., processes 2 2 , 3 3 , 5 5 , and 6 6 send messages. Next, process 4 4 receives the messages sent to it, combines the two corresponding values with its own value, and obtains the resulting partial result 5 + 6 + 4 = 15 5+6+4=15 , which it sends to its parent. Unfortunately, process 1 1 does not act likewise, because it has failed. Finally, process 0 0 receives the partial result 15 15 , and adds it to its local value of 0 0 . It does not receive any contribution from the left subtree.

[63] p: Things go differently when an up-correction phase is first executed. This is depicted in Figure 2 . Note that the numbering in the tree is different now. While it was arbitrarily chosen to be depth-first in Figure 1 , the numbering is now matching the numbering scheme for reduce, as described in Section 4.2 . Process 0 0 , the only one with a special role, did not change its position in the tree.

[64] p: In this example there are f = 1 f=1 failed processes, and in the up-correction algorithm processes exchange messages in groups of f + 1 = 2 f+1=2 . Processes 3 3 and 4 4 send messages to each other, as do processes 5 5 and 6 6 . Processes 1 1 and 2 2 would too, but since process 1 1 has failed, it does not send a message. Process 0 0 does not send any messages in this case, because n − 1 = 6 n-1=6 is divisible by f + 1 = 2 f+1=2 , and thus process 0 0 is not a member of any up-correction group. Upon receiving a message, each process updates its local value with the one sent to it. I.e., processes 3 3 and 4 4 hold the value 3 + 4 = 7 3+4=7 afterwards. Processes 5 5 and 6 6 store 5 + 6 = 11 5+6=11 . Processes 2 2 and 0 0 do not receive any message, and retain their original values.

[65] p: Next, the tree phase works like the tree algorithm described above, but all processes send the value obtained in the up-correction phase instead of their original value. Initially, processes 3 3 and 4 4 send 7 7 , and processes 5 5 and 6 6 send 11 11 . Next, process 2 2 receives the two messages sent to it, and computes the sum of their values and its own local value 7 + 11 + 2 = 20 7+11+2=20 . This result is sent to the root. Process 1 1 does not send any messages. Process 0 0 receives one message with the value 20 = 2 + 3 + 4 + 5 + 6 20=2+3+4+5+6 , and adds its local value 0 0 to it, to get the final result, 20 20 . Like before, process 1 1 did not get to contribute any value, because it failed before the operation. Unlike before, the children of process 1 1 did get to contribute their values. Since process 2 2 can include the information that there where no failures in its subtree, process 0 0 knows that the value it received is complete.

[66] p: Generally, the up-correction phase (described in Section 4.2 ), yields a single value, v v , in each process. The root is an exception if it is not part of the last group. If it is not, its value v v is its input value to reduce. For all other processes, v v is the result of reducing their input value with the input values of all other processes in the same up-correction group. The resulting value v v is used in the tree phase. Each process, except for the root, waits for messages from all their children, reduces their value with the local v v , and then sends the result to its parent. This is shown in pseudocode in algorithm 4 .

[67] p: If only the tree phase were executed, the root would get the results from combining the results from all subtrees of its child processes, if no failures occur. If up-correction is executed before, the root gets from each child process either the complete result, or the complete result without the value of the root, or the complete result without the values of the last group. The values of the last group are included if the last group has a member in the respective subtree. If root is a member of this group, its value is naturally included. In any case the root process has the information necessary to complete the result it gets from its children. Thus, the first answer that includes an indication that no failure happened in the respective subtree (more on that in Section 4.4 ) suffices for the root to compute the final result, and return from the call to reduce.

[68] h3: 4.4 Failure information

[69] p: The root receives multiple results. In the failure-free case, a correct result is sent by all children of the root, and the root can select any one. If processes fail, there can be incorrect results, and the root needs some information based on which it can select a correct value. Note that, corresponding to the semantics in Section 4.1 , different correct results are possible. If processes fail in-operational, no condition is made on whether they get to include their value. It is possible that both results – one including the value from an eventually failing process, and one without it – are sent to the root along different paths. This can, e.g., happen if a process completes the up-correction phase, but does not execute the subsequent tree phase.

[70] p: If only pre-operation occur, there is only one correct result.

[71] p: To enable the root to select a valid result, a failure description is accumulated in each subtree, and sent along with the reduction value. There are multiple options for this information.

[72] p: The failure description that provides the most information about failures to the root, at the cost of the highest potential message size, is sending a list of known failed processes. Note that in-operational failures can lead to a process appearing non-failed (contributing its value, and not being included in the list of failed processes), when in fact it fails shortly after. This can not be avoided, and it will potentially be detected in the next communication operation spanning this process (or never, if there is no such operation).

[73] p: In this scheme, in the up-correction phase and in the tree phase, each process appends the ids of all processes it can not receive a value from to a list of failed processes. This list is appended to the message that is sent to the parent in the tree phase and the parent adds the lists of its children to its own. In that way, the root receives a complete list of failed processes from each child that is known to have the complete reduction information, i.e., that does not contain a failed process in the subtree spanned by it.

[74] p: One potential use of the list of failed processes is to make that information available to all processes, to exclude failed processes in future operations. This is not described here further.

[75] p: A simplification of this scheme, that requires less data to be sent, at the expense of less information being available, is to only send the size of this list. Since the list is only appended to, without any regards to its content (note that items in lists that are concatenated always come from disjoint sets), the size can easily be tracked. To enable the root to choose which subtree’s value to select, each process needs to send along a bit to indicate whether a process failed in this subtree. This bit is set when a child is found to have failed in the tree.

[76] p: A third – even simpler – scheme is to only send a single failed bit. This bit is set in the tree phase, if a process does not receive a value from one of its children. It is not modified in the up-correction phase. The bit is equal to the ’local’ bit in the second scheme.

[77] p: That way, the root process only knows whether some failure happened in a subtree.

[78] h3: 4.5 Properties

[79] p: The goals of this section are to proof the semantics described in Section 4.1 , and to detail the number of messages that are required for reduce.

[80] h6: Definition .

[81] p: Let T T be a tree, f ∈ ℕ 0 f\in\mathbb{N}_{0} . Let r r be the root of T T . Then T T is an I(f)-tree , if

[82] p: r r has f + 1 f+1 children c 0 , … , c f c_{0},\ldots,c_{f} . The subtrees spanned by these vertices are called T 0 , … , T f T_{0},\ldots,T_{f} .

[83] p: For any two subtrees of the root T i , T j T_{i},T_{j} , i , j ∈ ℕ 0 i,j\in\mathbb{N}_{0} , i , j ≤ f i,j\leq f , the sizes of T i T_{i} and T j T_{j} differ by at most one.

[84] h6: Theorem 1 .

[85] p: Let there be no more then f f processes that experience a failure, in-operational or pre-operational. Let a I(f)-tree be used, with up-correction groups of size f + 1 f+1 .

[86] p: After up-correction, all values of non-failed processes, except for the values of processes grouped with root, are included exactly once in the final value available in each subtree of the root that does not indicate a failure after the tree phase.

[87] h6: Proof.

[88] p: First it is shown that the value from an arbitrary process is included at least once in each subtree. This is shown by constructing a process that has the value. Afterwards it is argued that there can not be multiple processes in one subtree that hold the value.

[89] p: Let ℓ \ell be a non-failed process, k ∈ ℕ 0 k\in\mathbb{N}_{0} , k > 0 k>0 , k ≤ f + 1 k\leq f+1 . It needs to be shown that the data from process ℓ \ell is available in the k k -th subtree, which is the subtree spanned by process numbered k k .

[90] p: If ℓ = 0 \ell=0 , it is the root, so it is considered “grouped with the root,” and there is nothing to show.

[91] p: Let ℓ \ell not be grouped with the root, i.e., ⌊ ℓ − 1 f + 1 ⌋ < ⌊ n − 1 f + 1 ⌋ \left\lfloor\frac{\ell-1}{f+1}\right\rfloor<\left\lfloor\frac{n-1}{f+1}\right\rfloor and ℓ ≠ 0 \ell\neq 0 . In up-correction ℓ \ell exchanges data with the process numbered a . . = ⌊ ℓ − 1 f + 1 ⌋ ​ ( f + 1 ) + k a\mathrel{\vbox{\hbox{\scriptsize.}\hbox{\scriptsize.}}}=\left\lfloor\frac{\ell-1}{f+1}\right\rfloor(f+1)+k (or a a is the number of ℓ \ell ).

[92] p: Then a < n a<n , and the process numbered a a is in the k k -th subtree, because ( a − 1 ) ​ mod ⁡ ( f + 1 ) = k − 1 (a-1)\xmod(f+1)=k-1 . If the process numbered a a does not fail at least long enough to send a message to its parent in the tree phase, its value is included in this message. Barring any failures along the way, the value is going to be included in the final result of the subtree. Thus the proof is complete in this case.

[93] p: If the process numbered a a , or any of its parents, experience a failure, and do not get to send a message in the tree phase, their respective parent detects the failure and propagates that information upward. Accordingly, the root of the subtree (i.e., the process numbered k k ) will not report no failures in its subtree.

[94] p: Note that additional failures can stop the propagation of this failure information. These additional failures will be detected, however, and will lead to process number k k not claiming “no failures.”

[95] p: This shows that there is a process in each given subtree that holds the value from process ℓ \ell . It remains to be shown that there is at most one.

[96] p: To see that at most one process in a different subtree receives the value from a given process, note that Communication for any process except for the root only occurs with at most one process from each other subtree. That holds because each process belongs to at most one up-correction group, and all communication except for the messages between the root of the tree and its children in the tree phase is within one subtree. ∎

[97] h6: Theorem 2 .

[98] p: Let there be no more then f f processes that experience a failure, in-operational or pre-operational. Let a I(f)-tree be used, with up-correction groups of size f + 1 f+1 .

[99] p: In the tree phase, all children of the root will either yield a correct value, or indicate a failure in their subtree, or have failed themselves.

[100] h6: Proof.

[101] p: In the tree phase, each non-failed process collects the messages from all its children and reduces the value received before sending a message itself. Thus, by Theorem 1 , subtrees without failures propagate all data. The value of (all) processes grouped with the root is included iff one such process is in the subtree in question.

[102] p: Now assume a failure does occur in the subtree in question. For ease of wording, assume first that the root of the subtree, i.e., the child of the root, has not failed. A failure in a subtree is guaranteed to lead to a failure being reported in the failure information sent together with the value by the root of the subtree, by the following logic. In the tree phase any process failure will eventually be detected by a non-failed parent, and be propagated by further non-failed parents. A failed parent will not propagate the failure information, but the next non-failed process will detect a failure.

[103] p: In this way, if the root of a subtree has not failed, it will report correctly on the presence of failures in its subtree.

[104] p: In case the respective child of the root failed, the theorem is trivially satisfied. The root will detect the failure, and classify the corresponding subtree as containing a failure. ∎

[105] p: When the root receives values from its children, it must select one of them, and potentially combine it with its own value. By Theorem 2 , it can select the value from any subtree without a failure. It knows which these are because all schemes for failure information propagation described before contain that information.

[106] h6: Theorem 3 .

[107] p: Let there be no more then f f processes that experience a failure, in-operational or pre-operational. Let a I(f)-tree be used, with up-correction groups of size f + 1 f+1 .

[108] p: After reduce either the root will have failed, or it will know the correct result, as described in Section 4.1 .

[109] h6: Proof.

[110] p: If no more than f f processes fail, at least one of the f + 1 f+1 children of root is guaranteed to have no failure in the subtree spanned by it.

[111] p: If the root has failed, the theorem is satisfied. Otherwise, by Theorem 2 , one child of the root will yield the correct value. The root might have to combine its value with its own value v v , depending on which child reported it. The root can detect a valid child to choose the value from because it does not report a failure in its subtree. ∎

[112] h6: Theorem 4 .

[113] p: Let there be no more then f f processes that experience a failure, in-operational or pre-operational. Let a I(f)-tree be used, with up-correction groups of size f + 1 f+1 .

[114] p: Reduce, as described in Section 4.3 , satisfies the semantics from Section 4.1 :

[115] p: If the root calls deliver_reduce( m m ) , all non-failed processes have called init_reduce( m m ) .

[116] p: Each process calls deliver_reduce( m m ) at most once for a given m m .

[117] p: The value returned by reduce at a non-failed root includes the input values of all non-failed processes.

[118] p: Values of failed processes are either included normally, or disregarded. No intermediate stages are possible.

[119] p: Each non-failed process executes deliver_reduce( m m ) eventually, if all non-failed processes execute init_reduce( m m ) .

[120] h6: Proof.

[121] p: This property follows from property 3. Note that failed process never calls deliver_reduce .

[122] p: Reduce is delivered once after the tree phase. It can not be skipped. Thus multiple receives are not possible.

[123] p: A leaf process, that does not receive in the tree phase, could theoretically execute it multiple times. It does not do so without external trigger, however, and a new call to reduce leads to a new unique id in the reduce message.

[124] p: This follows from Theorem 3 .

[125] p: Let p p be a failed process. If p p failed pre-operationally, it does not send any messages in the operation. Accordingly, the value of p p is not known to any non-failed processes, and is not included.

[126] p: Assume p p fails in-operationally. First assume that p p is not grouped with the root. Let S S be the subtree spanned by a child of the root that the root eventually selects the value from (cfg. Theorem 2 ). Then the result depends on the state of p p at the time of the sending operation to S S . The relevant sending operations are either the sending to the member of the up-correction group in S S , if p p is not in S S , or the message sent by p p to its parent, if p p is in S S .

[127] p: If p p does not fail before sending the respective message, its value is propagated normally, and is included in the result, like that of a non-failed process. If p p fails before sending that message, it is perceived like if it had failed pre-operationally. No value from p p is included in this case.

[128] p: If p p fails in-operationally and is grouped with the root (i.e., in the same up-correction group as the root), the reasoning is a little different. If p p is the root, its value is eventually disregarded, as nobody is going to receive the final message. If p p is not the root, either its message sent to the root in the up-correction phase plays the role of the message sent to a member of S S , if S S has no common member with the up-correction group of p p , or, if S S contains a member of the up-correction group of p p , called v v , the message from p p to v v plays that role.

[129] p: All that needs to be seen is that for some process p p the work between successive calls to reduce and deliver is bounded.

[130] p: First, in the up-correction phase, p p sends to and receives from all other processes in its up-correction group. These are up to f f processes. The receiving is retried if the failure monitor of the prospected sender confirms that it has not failed. Given that the process executes reduce , it will eventually either fail, in which case p p stops waiting for the message, or send a message, in which case p p will receive.

[131] p: The same holds for the subsequent tree phase. All non-failed children will eventually send, and p p will stop waiting for receives. After that, unless p p is the root, it will send a single message to its parent.

[132] p: ∎

[133] p: Note that in the presence of in-operation, item 4 of Theorem 4 allows for multiple different correct results. The root process gets to select the final result.

[134] h6: Theorem 5 .

[135] p: Let reduce be executed without any failures. Then the number of messages sent between computation processes is the following.

[136] p: In the up-correction phase f ⁡ ( f + 1 ) ​ ⌊ n − 1 f + 1 ⌋ + a ⁡ ( a − 1 ) f(f+1)\left\lfloor\frac{n-1}{f+1}\right\rfloor+a(a-1) with a = ( ( n − 1 ) ​ mod ⁡ ( f + 1 ) ) + 1 a=((n-1)\xmod(f+1))+1 are being sent.

[137] p: In the tree phase n − 1 n-1 messages are being sent.

[138] p: This does not include any messages that might be necessary for the detection of failures. These can even be required when no failures occur.

[139] p: When processes fail, less messages are being sent.

[140] h6: Proof.

[141] p: First consider the failure-free case.

[142] p: There are ⌊ n − 1 f + 1 ⌋ \left\lfloor\frac{n-1}{f+1}\right\rfloor up-correction groups with f + 1 f+1 processes each. In each such group each of the f + 1 f+1 processes sends f f messages. That accounts for the first term.

[143] p: If a > 1 a>1 , it is the size of the last up-correction group. a ⁡ ( a − 1 ) a(a-1) is the number of messages sent in this group, because each of the processes sends a − 1 a-1 messages. If a = 1 a=1 , there is no additional up-correction group, but a ⁡ ( a − 1 ) = 0 a(a-1)=0 .

[144] p: In the tree phase each process except for the root sends one message to its parent in the tree.

[145] p: If there are failures, the failing processes send less messages. Perhaps none, if the process failed pre-operational. No other process sends more messages based on failures.

[146] p: ∎

[147] h2: 5 Allreduce

[148] p: Without failures, allreduce works like reduce, but the result is provided at all processes. There is no root process in allreduce.

[149] p: Allreduce is one of the most common operations in HPC programs [ 8 ] , and is frequently studied [ 5 , 7 , 9 ] .

[150] p: THe algorithm for allreduce is consecutive execution of reduce to an arbitrary root and broadcast from this root. Some consideration has to be given the case of a failed root. The short version is that the fault tolerance of reduce and broadcast yield the required properties for allreduce. The long version is detailed below.

[151] p: The following notation is used. Analogous to reduce, an allreduce operation is identified by an allreduce message m m . The content of m m is defined below. Each process executes init_allreduce( m m ) before sending any network message related to the allreduce operation, and deliver_allreduce( m m ) to signal completion of the operation to the caller.

[152] p: The allreduce message does not store a root process, as there is no dedicated root in allreduce. Instead it has the following members:

[153] p: The set of processes that participate in the operation.

[154] p: A unique id.

[155] p: The value. This is only relevant for the call to deliver , as no final value is available at the time allreduce is called.

[156] h3: 5.1 Semantics

[157] p: Let n n processes execute allreduce. Let up to f f processes fail, pre-operationally or in-operationally. A set of at least f + 1 f+1 processes must be known to only fail pre-operationally, not in-operationally.

[158] p: Then, if all processes execute allreduce, the following semantics hold.

[159] p: If any process calls deliver_allreduce( m m ) , all non-failed processes have called init_allreduce( m m ) .

[160] p: Each process calls deliver_reduce( m m ) at most once for a given m m .

[161] p: Each non-failed process calls deliver_allreduce m m eventually, if all non-failed processes called init_allreduce( m m ) .

[162] p: Each allreduce includes the values of all non-failed processes.

[163] p: The value of a failed process is either included at every non-failed process, or at none.

[164] p: This is proven in Section 5.3 .

[165] h3: 5.2 Description

[166] figure: Input: The data contributed by this process Output: The result, including contributions of all non-failed processes function allreduce( data ) begin r ← 0 \leftarrow 0 ok ← \leftarrow false while not ok do allreduce_data ← \leftarrow reduce( data , root=r) result ← \leftarrow broadcast( allreduce_data , root=r) ok ← \leftarrow broadcast finished successfully r ← \leftarrow successor(r) end while return result end Algorithm 5 Allreduce

[167] p: As described above, this algorithm consists of a fault-tolerant reduce to an arbitrary root, followed by a fault-tolerant broadcast of the resulting value from this root. The algorithm is shown in algorithm 5 . Broadcast and reduce need to satisfy the semantics described in the paper on fault tolerant broadcast [ 6 ] and Section 4.1 .

[168] p: Since there is no root process in allreduce, the root is chosen arbitrarily. The scheme requires the root to be chosen consistently across all participating processes, and from the set of processes that are known not to fail in-operationally. The reason for this restriction is the corresponding requirement of broadcast.

[169] p: If the root does not fail pre-operationally, the operation completes. Otherwise, the failure is consistently detected, and a new root is chosen.

[170] p: To guarantee progress, at least f + 1 f+1 processes must eventually be tried as root. Therefor a deterministic selection that selects enough processes eventually is needed.

[171] h3: 5.3 Properties

[172] h6: Theorem 6 .

[173] p: Given reduce and broadcast that satisfy the semantics in Section 4.1 and the paper on fault tolerant broadcast, respectively, allreduce, as described in Section 5.2 , satisfies the semantics from Section 5.1 :

[174] p: If any process calls deliver_allreduce( m m ) , all non-failed processes have called init_allreduce( m m ) .

[175] p: Each process calls deliver_reduce( m m ) at most once for a given m m .

[176] p: Each non-failed process calls deliver_allreduce m m eventually, if all non-failed processes called init_allreduce( m m ) .

[177] p: Each allreduce includes the values of all non-failed processes.

[178] p: The value of a failed process is either included at every non-failed process, or at none.

[179] h6: Proof.

[180] p: Without loss of generality, assume that there is a process that does not fail until the end of the operation. Otherwise the semantics are trivially satisfied.

[181] p: Calling deliver_allreduce implies having called deliver_reduce for the root process, and deliver_broadcast for all other processes. Thus, property 1 of both operations semantics yield this property.

[182] p: Like property 1, this is a direct consequence of the corresponding properties of reduce and broadcast.

[183] p: First reduce is executed which is delivered eventually, by property 5 of the semantics of reduce.

[184] p: If the root has not failed, it sends a normal broadcast, and property 3 and 5 of the semantics of broadcast gives this property.

[185] p: If the root has failed, it is detected, and a new root is tried. Because f + 1 f+1 candidates are available at least one process does not fail, and a non-failed root is tried eventually.

[186] p: The value of the allreduce is the value that is sent in the broadcast, which is received by the root in the previous reduce. Property 3 of the semantics of reduce thus provides this property.

[187] p: Whether the value of a failed process are included in the result of the reduce to the root process is unspecified. But no intermediate state is possible, by property 4 of the semantics of reduce. Since a single root is used to determine the value of the allreduce, its value provides a consistent result for all other processes.

[188] p: ∎

[189] h6: Theorem 7 .

[190] p: If the root did and does not fail, allreduce as described in Section 5.2 requires as many messages to be sent between computation processes, as reduce together with broadcast does.

[191] p: f f failures can increase this number at most to the ( f + 1 ) (f+1) -fold.

[192] h6: Proof.

[193] p: If the root has not failed, reduce and broadcast are executed in succession. No additional messages are sent.

[194] p: If the root failed, no additional messages are sent, and the operation is retried with a new root. f f failures can lead to at most f + 1 f+1 roots tried, and thus f + 1 f+1 times the amount of messages. ∎

[195] h2: References

[196] h2: Instructions for reporting errors

[197] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[198] p: Tip: You can select the relevant text first, to include it in your report.

[199] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[200] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
