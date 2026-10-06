
# Replication Data for: GPRat: Gaussian Process Regression with Asynchronous Tasks

This repository complements the identically titled paper submitted to WAMTA 2025 and allows the reproduction of the published results.

## Related Publication:

Python is the de-facto language for software development in artificial intelligence (AI). Commonly used libraries, such as PyTorch and TensorFlow, rely on parallelization built into their BLAS backends to achieve speedup on CPUs. However, only applying parallelization in a low-level backend can lead to performance and scaling degradation. 
In this work, we present a novel way of binding task-based \CPP code built on the asynchronous runtime model HPX to a high-level Python API using pybind11. We develop a parallel Gaussian process (GP) library as an application. The resulting Python library GPRat combines the ease of use of commonly available GP libraries with the performance and scalability of asynchronous runtime systems.
We evaluate the performance on a mass-spring-damper system, a standard benchmark from control theory, with varying numbers of regressors (features). Results show almost no overhead when binding the asynchronous HPX code using pybind11. Compared to GPyTorch and GPflow, GPRat shows superior scaling on up to 64 cores on an AMD EPYC 7742 CPU for training. Furthermore, our library achieves a prediction speedup of up to factor 7.63 over GPyTorch and 25.25 over GPflow. If we increase the number of features from eight to 128, we observe speedups of up to factor 29.62 and 21.19, respectively.
These results showcase the potential of using asynchronous tasks within Python-based AI applications.

## Data

This dataset contains the simulated data of a coupled mass-spring-damper system. We provide the same input and output data for training and testing we used for our benchmark. Note that both training and test data sets have a size of 2^19. If larger data sets are required, they can be generated with the mass-spring-damper simulator integrated into GPRat.

## Software Versions

All required software can be installed with `spack` and `pip`.

### GPRat

We provide scripts with GPRat `v0.1.0` that install all dependencies to manually build GPRat with `spack`.
Nonetheless, we include the spack environment explicitly in this document:

```
spack:
	specs:
	- hpx@1.10.0%gcc +static malloc=system networking=none max_cpu_count=256 instrumentation=none
	^cmake@3.30 ^curl@8.10.1 ^ninja@1.12.1
	- intel-oneapi-mkl@2024.2.1%gcc shared=false
	view: true
	concretizer:
		unify: true
```

Note that to build HPX with static linking at the time of writing, it is necessary to add the spack-repo of GPRat to `spack`. We recommend using GCC `14.2.0` to reproduce our results exactly.

  

### Reference Implementations

We provide scripts to automatically create a dedicated environment and run the reference code with GPflow and GPyTorch in Python. Nonetheless, we include an explicit requirement list in this document.

```
# GPyTorch
gpytorch==1.13
```

```
# GPflow
gpflow==2.9.2 (installed manually with MKL patch)
intel-tensorflow==2.13.0
numpy==1.24.3
gast==0.4.0
tensorflow-probability==0.21.0
typing-extensions==4.5.0
```

Note that GPflow without MKL support can be also installed directly with `pip`. We recommend Python 3.8.0 to reproduce our results exactly.

## Bechmarking  

The `examples` directory of GPRat contains a benchmarking example for each implementation.
Add the data provided in this supplementary material and change the `config.json` files. Then simply run the execution scripts.