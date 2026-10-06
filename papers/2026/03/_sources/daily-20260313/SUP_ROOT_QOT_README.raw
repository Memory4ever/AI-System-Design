# Questions-of-Thought (QoT) Framework

The **Questions-of-Thought (QoT)** framework is a systematic algorithm designed to decompose a goal into sequential steps and solve each step by leveraging a chain of questions. This structured approach ensures that intermediate reasoning is recorded and updated progressively, enabling efficient and comprehensive problem-solving.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Algorithm](#algorithm)
- [Usage](#usage)
- [License](#license)

---

## Introduction

The **Questions-of-Thought (QoT)** framework introduces a methodical way to tackle complex problems by:
1. **Decomposing** the main goal into \( n \) ordered steps.
2. **Generating QA Chains** for each step, with each chain containing \( m_i \) questions.
3. **Step-by-step problem solving**, where:
   - Each question is solved sequentially.
   - Results are recorded in the **Thinking Process**.
   - The **Response** is updated after solving each question.

This approach balances context preservation (using the Thinking Process) and simplicity in outputs (updating the Response).

---

## Features

- **Goal Decomposition**: Break a complex goal into manageable, ordered steps.
- **QA Chain for Each Step**: Structure reasoning into chains of questions.
- **Context-Aware Reasoning**: Solutions take into account the cumulative Thinking Process.
- **Progressive Response Updates**: Responses are updated in real time without dependency on historical outputs.
- **Time-Sequential Workflow**: Ideal for multi-turn reasoning and problem-solving tasks.

---

## Architecture

The QoT framework consists of the following key components:

1. **Goal and Steps**:
   - The input goal is decomposed into \( n \) sequential steps:  
     \[
     Steps = \{S_1, S_2, \dots, S_n\}
     \]

2. **QA Chain**:
   - Each step \( S_i \) is associated with a QA Chain containing \( m_i \) questions:  
     \[
     QA_i = \{Q_{i,1}, Q_{i,2}, \dots, Q_{i,m_i}\}
     \]

3. **Thinking Process**:
   - A cumulative log of all solutions, ensuring full context for reasoning:
     \[
     TP_{t+1} = TP_t \cup \text{Solve}(Q_{i,j}, TP_t)
     \]

4. **Response**:
   - A progressive summary of results, updated in real time based on the current solution:
     \[
     R_{t+1} = \text{Update}(R_t, \text{Solve}(Q_{i,j}, TP_t))
     \]

---

## Algorithm

### Step-by-Step Execution:

1. **Initialization**:
   - Start with empty Thinking Process and Response:
     \[
     TP_0 = \emptyset, \quad R_0 = \emptyset
     \]

2. **Iterative Question Solving**:
   - For each step \( S_i \), process its QA Chain \( QA_i \):
     \[
     TP_{t+1} = TP_t \cup \text{Solve}(Q_{i,j}, TP_t)
     \]
     \[
     R_{t+1} = \text{Update}(R_t, \text{Solve}(Q_{i,j}, TP_t))
     \]

3. **Repeat for All Steps**:
   - Solve all questions in \( QA_1 \), followed by \( QA_2 \), and so on until \( QA_n \) is complete.

4. **Final Output**:
   - The final Response \( R \) contains the complete solution:
     \[
     R = \text{Final Response}.
     \]

---

## Usage

This framework can be applied to various domains, such as:
- **Multi-turn dialogue systems**: Reasoning over a series of conversational turns.
- **Problem-solving tasks**: Decomposing complex problems into smaller steps.
- **Task planning and execution**: Breaking down large goals into actionable subtasks.


---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to adapt this README to match the specific implementation details or audience for your project!
