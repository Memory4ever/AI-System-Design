+## http://arxiv.org/abs/2603.08593v1

A GPU-Accelerated Transient Detection Pipeline for DECam Time-Domain Surveys

We present a GPU-accelerated transient detection pipeline developed for time-domain surveys with the Dark Energy Camera (DECam). It enables real-time-capable image processing, incorporating science-driven candidate filtering to support rapid transient identification in time-critical observing programs. The pipeline serves as the core transient discovery engine for multiple long-term DECam programs, including the GW-MMADS gravitational-wave follow-up campaign and the DESIRT survey for intermediate-redshift transients with DESI synergy. The pipeline ingests calibrated imaging products from the DECam Community Pipeline and performs image differencing using the SFFT algorithm, coupled with CNN-based real-bogus classification, to produce science-ready transient alerts and light curves that are delivered to community brokers. We validate the pipeline using archival DECam data from the DESIRT survey. The real-bogus classifier achieves a completeness of $\sim$ 99\% of real transients while rejecting $\sim$ 96\% of subtraction artifacts, and the workflow typically reduces the candidate load to a manageable level for survey operations. With GPU acceleration, the typical processing time per DECam exposure is $\sim$ 50 s from calibrated image processing to alert generation using a modest allocation of computing resources.

## http://arxiv.org/abs/2603.07764v1

Using GPUs And LLMs Can Be Satisfying for Nonlinear Real Arithmetic Problems

Solving quantifier-free non-linear real arithmetic (NRA) problems is a computationally hard task. To tackle this problem, prior work proposed a promising approach based on gradient descent. In this work, we extend their ideas and combine LLMs and GPU acceleration to obtain an efficient technique. We have implemented our findings in the novel SMT solver GANRA (GPU Accelerated solving of Nonlinear Real Arithmetic problems). We evaluate GANRA on two different NRA benchmarks and demonstrate significant improvements over the previous state of the art. In particular, on the Sturm-MBO benchmark, we can prove satisfiability for more than five times as many instances in less than 1/20th of the previous state-of-the-art runtime.

