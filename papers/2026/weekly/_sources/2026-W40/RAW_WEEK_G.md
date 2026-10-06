CUDA Toolkit 13.2 Update 2 - Release Notes — Release Notes 13.2 documentation (https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html)
citeturn29550view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html#overview","lineno":null}); Total lines: 920
L0: [Input: Search docs] [Input] [Input]
L1: 
L2: cite0†Release Notes L3: 
L4: CUDA Toolkit 13.2 Update 2 - Release Notes
L5: # 1. Overviewcite1† L6: 
L7: Welcome to the release notes for NVIDIA® CUDA® Toolkit 13.2 Update 2. This release includes enhancements and fixes across the CUDA Toolkit and its libraries.
L8: 
L9: Note
L10: CUDA Toolkit 13.2 Update 2 resolves two critical issues that could produce incorrect results: a cuBLAS bug, introduced in 13.2 Update 1, where `cublasLtMatmul()` could ignore tensor-wide scaling for NVFP4 matrix multiplications (see the cite2†cuBLAS resolved issue ); and a compiler bug, present since CUDA 12.8, where failed thread reconvergence could leave stale or corrupted register values in kernels with nested thread divergence (see the cite3†compiler resolved issue ).
L11: If you cannot move to Update 2, a cuBLAS patch (13.4.1) is available for the cuBLAS issue — see the cite4†cuBLAS patch release notes .
L12: This documentation is organized into two main sections:
L13: 
L14:   * General CUDA
L15: 
L16: Focuses on the core CUDA infrastructure including component versions, driver compatibility, compiler/runtime features, issues, and deprecations.
L17: 
L18:   * CUDA Libraries
L19: 
L20: Covers the specialized computational libraries with their feature updates, performance improvements, API changes, and version history across CUDA 13.x releases.
L21: # 2. General CUDAcite5† L22: ## 2.1. CUDA Toolkit Major Componentscite6† L23: 
L24: > Note
L25: >
L26: > Starting with CUDA 11, individual components within the CUDA Toolkit (for example: compiler, libraries, tools) are versioned independently.
L27: >
L28: > For CUDA 13.2 Update 2, the table below indicates the versions:
L29: Table 1 CUDA 13.2 Update 2 Component Versionscite7† L30: Component Name  | Version Information  | Supported Architectures  | Supported Platforms
L31: --- | --- | --- | ---
L32: CUDA C++ Core Compute Libraries  | Thrust  | 3.2.0  | x86_64, arm64-sbsa  | Linux, Windows
L33: CUB  | 3.2.0
L34: libcu++  | 3.2.0
L35: Cooperative Groups  | 13.2.86
L36: CUDA Application Compiler (crt)  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L37: CUDA Compilation Optimizer (ctadvisor)  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L38: CUDA Runtime (cudart)  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L39: CUDA culibos  | 13.2.86  | x86_64, arm64-sbsa  | Linux
L40: CUDA cuobjdump  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows
L41: CUPTI  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L42: CUDA cuxxfilt (demangler)  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows
L43: CUDA Documentation  | 13.2.86  | x86_64  | Linux, Windows
L44: CUDA GDB  | 13.2.86  | x86_64, arm64-sbsa  | Linux, WSL
L45: CUDA Nsight Eclipse Plugin  | 13.2.86  | x86_64  | Linux
L46: CUDA NVCC  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L47: CUDA nvdisasm  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows
L48: CUDA NVML Headers  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L49: CUDA nvprune  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L50: CUDA NVRTC  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L51: CUDA NVTX  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L52: CUDA OpenCL  | 13.2.86  | x86_64  | Linux, Windows
L53: CUDA Profiler API  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L54: CUDA Sandbox dev  | 13.2.86  | x86_64, arm64-sbsa  | Linux, WSL
L55: CUDA Compute Sanitizer API  | 13.2.87  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L56: CUDA TILE-IR AS  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L57: CUDA cuBLAS  | 13.4.1.3  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L58: CUDA cuDLA  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L59: CUDA cuFFT  | 12.2.0.57  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L60: CUDA cuobjclient  | 1.1.1.22  | x86_64, arm64-sbsa  | Linux
L61: CUDA cuFile  | 1.17.1.22  | x86_64, arm64-sbsa  | Linux
L62: CUDA cuRAND  | 10.4.2.66  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L63: CUDA cuSOLVER  | 12.2.0.11  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L64: CUDA cuSPARSE  | 12.7.10.12  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L65: CUDA NPP  | 13.1.0.59  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L66: CUDA nvFatbin  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L67: CUDA nvJitLink  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L68: CUDA nvJPEG  | 13.1.0.59  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L69: CUDA nvptxcompiler  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L70: CUDA nvvm  | 13.2.86  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L71: Nsight Compute  | 2026.1.1.2  | x86_64, arm64-sbsa  | Linux, Windows, WSL (Windows 11)
L72: Nsight Systems  | 2025.6.3.541  | x86_64, arm64-sbsa  | Linux, Windows, WSL
L73: Nsight Visual Studio Edition (VSE)  | 2026.1.0.25345  | x86_64 (Windows)  | Windows
L74: nvidia_fscite8†1 | 2.28.4  | x86_64, arm64-sbsa  | Linux
L75: nvlsm  | 2025.10.12  | x86_64, arm64-sbsa  | Linux
L76: Visual Studio Integration  | 13.2.86  | x86_64 (Windows)  | Windows
L77: NVIDIA Linux Driver  | 595.71.05  | x86_64, arm64-sbsa  | Linux
L78: ## 2.2. CUDA Drivercite9† L79: > Running a CUDA application requires the system with at least one CUDA capable GPU and a driver that is compatible with the CUDA Toolkit. See cite10†Table 3 . For more information various GPU products that are CUDA capable, visit cite11†https://developer.nvidia.com/cuda-gpus†developer.nvidia.com .
L80: >
L81: > Each release of the CUDA Toolkit requires a minimum version of the CUDA driver. The CUDA driver is backward compatible, meaning that applications compiled against a particular version of the CUDA will continue to work on subsequent (later) driver releases.
L82: >
L83: > More information on compatibility can be found at cite12†https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#cuda-compatibility-and-upgrades .
L84: >
L85: > Note: Starting with CUDA 11.0, the toolkit components are individually versioned, and the toolkit itself is versioned as shown in the table below.
L86: >
L87: > The minimum required driver version for CUDA minor version compatibility is shown below. CUDA minor version compatibility is described in detail in cite13†https://docs.nvidia.com/deploy/cuda-compatibility/index.html L88: Table 2 CUDA Toolkit and Minimum Required Driver Version for CUDA Minor Version Compatibilitycite14† L89: CTK Version  | Driver Range for Minor Version Compatibility
L90: --- | ---
L91:  | Min  | Max
L92: --- | --- | ---
L93: 13.x  | >= 580  | N/A
L94: 12.x  | >= 525  | < 580
L95: 11.x  | >= 450  | < 525
L96: 
L97: * Using a Minimum Required Version that is different from Toolkit Driver Version could be allowed in compatibility mode – please read the CUDA Compatibility Guide for details.
L98: ** Starting with CUDA 13.1, the Windows display driver is no longer bundled with the CUDA Toolkit package. Users must download and install the appropriate NVIDIA driver separately from the official driver download page.
L99: 
L100: For more information on supported driver versions, see the cite13†CUDA Compatibility Guide for drivers.
L101: *** CUDA 11.0 was released with an earlier driver version, but by upgrading to Tesla Recommended Drivers 450.80.02 (Linux) / 452.39 (Windows), minor version compatibility is possible across the CUDA 11.x family of toolkits.
L102: 
L103: The version of the development NVIDIA GPU Driver packaged in each CUDA Toolkit release is shown below.
L104: 
L105: cite15†1 L106: 
L107: 
L108: Only available on select Linux distros
L109: Table 3 CUDA Toolkit and Corresponding Driver Versionscite16† L110: CUDA Toolkit  | Toolkit Driver Version
L111: --- | ---
L112:  | Linux x86_64 Driver Version  | Windows x86_64 Driver Version
L113: CUDA 13.2 Update 2  | >=595.71.05  | N/A
L114: CUDA 13.2 Update 1  | >=595.58.03  | N/A
L115: CUDA 13.2 GA  | >=595.45.04  | N/A
L116: CUDA 13.1 Update 1  | >=590.48.01  | N/A
L117: CUDA 13.1 GA  | >=590.44.01  | N/A
L118: CUDA 13.0 Update 2  | >=580.95.05  | N/A
L119: CUDA 13.0 Update 1  | >=580.82.07  | N/A
L120: CUDA 13.0 GA  | >=580.65.06  | N/A
L121: CUDA 12.9 Update 1  | >=575.57.08  | >=576.57
L122: CUDA 12.9 GA  | >=575.51.03  | >=576.02
L123: CUDA 12.8 Update 1  | >=570.124.06  | >=572.61
L124: CUDA 12.8 GA  | >=570.26  | >=570.65
L125: CUDA 12.6 Update 3  | >=560.35.05  | >=561.17
L126: CUDA 12.6 Update 2  | >=560.35.03  | >=560.94
L127: CUDA 12.6 Update 1  | >=560.35.03  | >=560.94
L128: CUDA 12.6 GA  | >=560.28.03  | >=560.76
L129: CUDA 12.5 Update 1  | >=555.42.06  | >=555.85
L130: CUDA 12.5 GA  | >=555.42.02  | >=555.85
L131: CUDA 12.4 Update 1  | >=550.54.15  | >=551.78
L132: CUDA 12.4 GA  | >=550.54.14  | >=551.61
L133: CUDA 12.3 Update 1  | >=545.23.08  | >=546.12
L134: CUDA 12.3 GA  | >=545.23.06  | >=545.84
L135: CUDA 12.2 Update 2  | >=535.104.05  | >=537.13
L136: CUDA 12.2 Update 1  | >=535.86.09  | >=536.67
L137: CUDA 12.2 GA  | >=535.54.03  | >=536.25
L138: CUDA 12.1 Update 1  | >=530.30.02  | >=531.14
L139: CUDA 12.1 GA  | >=530.30.02  | >=531.14
L140: CUDA 12.0 Update 1  | >=525.85.12  | >=528.33
L141: CUDA 12.0 GA  | >=525.60.13  | >=527.41
L142: CUDA 11.8 GA  | >=520.61.05  | >=520.06
L143: CUDA 11.7 Update 1  | >=515.48.07  | >=516.31
L144: CUDA 11.7 GA  | >=515.43.04  | >=516.01
L145: CUDA 11.6 Update 2  | >=510.47.03  | >=511.65
L146: CUDA 11.6 Update 1  | >=510.47.03  | >=511.65
L147: CUDA 11.6 GA  | >=510.39.01  | >=511.23
L148: CUDA 11.5 Update 2  | >=495.29.05  | >=496.13
L149: CUDA 11.5 Update 1  | >=495.29.05  | >=496.13
L150: CUDA 11.5 GA  | >=495.29.05  | >=496.04
L151: CUDA 11.4 Update 4  | >=470.82.01  | >=472.50
L152: CUDA 11.4 Update 3  | >=470.82.01  | >=472.50
L153: CUDA 11.4 Update 2  | >=470.57.02  | >=471.41
L154: CUDA 11.4 Update 1  | >=470.57.02  | >=471.41
L155: CUDA 11.4.0 GA  | >=470.42.01  | >=471.11
L156: CUDA 11.3.1 Update 1  | >=465.19.01  | >=465.89
L157: CUDA 11.3.0 GA  | >=465.19.01  | >=465.89
L158: CUDA 11.2.2 Update 2  | >=460.32.03  | >=461.33
L159: CUDA 11.2.1 Update 1  | >=460.32.03  | >=461.09
L160: CUDA 11.2.0 GA  | >=460.27.03  | >=460.82
L161: CUDA 11.1.1 Update 1  | >=455.32  | >=456.81
L162: CUDA 11.1 GA  | >=455.23  | >=456.38
L163: CUDA 11.0.3 Update 1  | >= 450.51.06  | >= 451.82
L164: CUDA 11.0.2 GA  | >= 450.51.05  | >= 451.48
L165: CUDA 11.0.1 RC  | >= 450.36.06  | >= 451.22
L166: CUDA 10.2.89  | >= 440.33  | >= 441.22
L167: CUDA 10.1 (10.1.105 general release, and updates)  | >= 418.39  | >= 418.96
L168: CUDA 10.0.130  | >= 410.48  | >= 411.31
L169: CUDA 9.2 (9.2.148 Update 1)  | >= 396.37  | >= 398.26
L170: CUDA 9.2 (9.2.88)  | >= 396.26  | >= 397.44
L171: CUDA 9.1 (9.1.85)  | >= 390.46  | >= 391.29
L172: CUDA 9.0 (9.0.76)  | >= 384.81  | >= 385.54
L173: CUDA 8.0 (8.0.61 GA2)  | >= 375.26  | >= 376.51
L174: CUDA 8.0 (8.0.44)  | >= 367.48  | >= 369.30
L175: CUDA 7.5 (7.5.16)  | >= 352.31  | >= 353.66
L176: CUDA 7.0 (7.0.28)  | >= 346.46  | >= 347.62
L177:   * CUDA Toolkit driver bundling (pre-CUDA 13.1):
L178: 
L179:     * The CUDA Toolkit previously included an NVIDIA display driver for convenience.
L180: 
L181:     * This bundled driver was intended only for development purposes.
L182: 
L183:     * It is not recommended for production use, especially with Tesla GPUs.
L184: 
L185:   * Recommended driver for Tesla GPUs:
L186: 
L187:     * For production environments using Tesla GPUs, download the latest certified driver from the official NVIDIA Driver Downloads site:
L188: cite17†https://www.nvidia.com/drivers†www.nvidia.com L189: 
L190:   * Optional driver installation during Toolkit setup:
L191: 
L192:     * During CUDA Toolkit installation, users may choose to skip driver installation:
L193: 
L194:       * On Windows: via interactive or silent install options.
L195: 
L196:       * On Linux: by skipping driver meta packages.
L197: 
L198:   * Change in CUDA 13.1 (Windows-specific):
L199: 
L200:     * Starting with CUDA 13.1, the Windows display driver is no longer bundled with the CUDA Toolkit.
L201:     * Windows users must manually download and install the appropriate driver from the official NVIDIA site.
L202: 
L203:   * Driver compatibility notes:
L204: 
L205:     * Some compatibility tables may list “N/A” for Windows driver versions.
L206: 
L207:     * Users must still ensure the installed driver meets or exceeds the minimum required version for the CUDA Toolkit.
L208: 
L209:     * For details, refer to the official CUDA Compatibility Guide for Drivers:
L210: 
L211: > cite13†https://docs.nvidia.com/deploy/cuda-compatibility/index.html L212: ## 2.3. New Featurescite18† L213: 
L214: General CUDA
L215: 
L216:   * No new features in this release.
L217: 
L218: CUDA Compiler
L219: 
L220: >   * For new features from PTX, refer to cite19†PTX ISA version 9.2 .
L221: 
L222: ### 2.3.1. CUDA Developer Toolscite20† L223: 
L224: For details on new features, improvements, and bug fixes, see the changelogs for:
L225: 
L226:   * cite21†Nsight Systems .
L227: 
L228:   * cite22†Nsight Visual Studio Edition .
L229: 
L230:   * cite23†CUPTI .
L231: 
L232:   * cite24†Nsight Compute .
L233: 
L234:   * cite25†Compute Sanitizer .
L235: 
L236:   * cite26†CUDA-C++-Programming-Guide .
L237: 
L238: ## 2.4. Resolved Issuescite27† L239: ### 2.4.1. CUDA Compilercite28† L240: 
L241:   * Fixed a compiler issue, present since CUDA 12.8, that could cause compiler-inserted thread reconvergence to fail and leave stale or corrupted values in registers, resulting in incorrect program execution. This issue could occur only in kernels that contain two or more nested levels of thread divergence where the compiler elided convergence instructions for one or more divergence levels. Kernels with only a single level of divergence are unaffected.[6111901]
L242: Minimal illustrative example:
L243: 
L244:     __global__ void affected(const int* in, int* out) {
L245:         int tid = threadIdx.x;
L246: 
L247:         if (tid < 16) {             // Level 1 divergence
L248:             if (in[tid] > 0) {      // Level 2 divergence, nested
L249:                 // If the compiler elides reconvergence for one of these
L250:                 // divergence levels, a register written in this region
L251:                 // can carry a stale value across the reconvergence point.
L252:                 out[tid] = compute(in[tid]);
L253:             }
L254: 
L255:             // Implicit reconvergence: failure can manifest here.
L256:         }
L257:     }
L258: ## 2.5. Known Issuescite29† L259: ### 2.5.1. General CUDAcite30† L260: 
L261:   * On SLES 16 systems used for NVLink 5 testing, NVIDIA Fabric Manager may fail to start when DOCA OFED is installed.
L262: 
L263: Symptom:
L264: 
L265: NVIDIA Fabric Manager fails to start on SLES 16 systems used for NVLink 5 testing when DOCA OFED is installed.
L266: 
L267: Problem Description:
L268: 
L269: This issue can occur because the `ib_core` module is provided by both the SLES 16 kernel and DOCA OFED, which can lead to a module conflict.
L270: 
L271: Workaround:
L272: Unload the SLES 16 kernel-provided `ib_core` module and load the DOCA OFED-provided `ib_core` module instead. After loading the DOCA OFED-provided module, NVIDIA Fabric Manager starts and the system operates correctly.
L273: 
L274:   * CUDA initialization can fail on certain Linux kernels with KASLR enabled.
L275: 
L276: Symptom:
L277: CUDA initialization fails. This issue is indicated by the following debug message:
L278: 
L279:     [64689.125237] nvidia-uvm: uvm_pmm_gpu.c:3176 devmem_alloc_pagemap[pid:92821] request_free_mem_region() err -34
L280: 
L281: 
L282: Problem Description:
L283: 
L284: Certain Linux kernels have a known issue in HMM initialization when KASLR is enabled.
L285: 
L286: Workaround:
L287: 
L288: Fixes for this issue are being handled in upstream kernels. In the meantime, you can use one of the following workarounds:
L289: 
L290:     * Option 1: Disable KASLR (preferred option)
L291: If using GRUB, edit `/etc/default/grub` and add `nokaslr` to `GRUB_CMDLINE_LINUX_DEFAULT`:
L292: 
L293:         GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nokaslr"
L294: 
L295: 
L296: Then update GRUB and reboot:
L297: 
L298:         sudo update-grub
L299:         sudo reboot
L300: 
L301: 
L302:     * Option 2: Disable HMM for UVM
L303: 
L304:       1. Create or edit `/etc/modprobe.d/uvm.conf`.
L305: 
L306:       2. Add or update the following line:
L307: 
L308:             options nvidia_uvm uvm_disable_hmm=1
L309:       3. Unload and reload the `nvidia_uvm` kernel module, or reboot the system:
L310: 
L311:             sudo modprobe -r nvidia_uvm
L312:             sudo modprobe nvidia_uvm
L313: ### 2.5.2. CUDA Compilercite31† L314: 
L315:   * Data Race in WGMMA A/B Register Copy Propagation
L316: 
L317: Symptom:
L318: 
L319: Kernels that use `wgmma.mma_async` with `wgmma.wait_group.sync.aligned N` where `N >= 1` can produce incorrect numerical results when `mov` instructions are intentionally placed after the wait to prevent WGMMA input registers from being overwritten by in-flight HGMMAs.
L320: 
L321: Problem Description:
L322: In pipelined warp-group MMA loops, `mov.b32` instructions are sometimes intentionally placed after `wgmma.wait_group.sync.aligned N` where `N > 0` to ensure that WGMMA input registers are not overwritten while HGMMAs from the previous iteration are still in flight. In this case, the compiler can incorrectly copy-propagate across `wgmma.wait_group.sync.aligned N` and eliminate those `mov` instructions.
L323: For example, in the following pattern, `ldmatrix.x4` feeds two consecutive WGMMA calls. The compiler eliminates the second `mov`, exposing the race:
L324: 
L325:     $loop:
L326:         ldmatrix.sync.aligned.m8n8.x4.shared.b16 {%r71, %r91, %r81, %r101}, [%r8];
L327: 
L328:         mov.b32 %r70, %r71;
L329:         wgmma.fence.sync.aligned;
L330:         wgmma.mma_async { }, {%r70, ..}, ...;
L331:         wgmma.commit_group.sync.aligned;
L332:         wgmma.wait_group.sync.aligned 1;
L333:         mov.b32 %r80, %r81;                    // compiler eliminates this mov
L334:         wgmma.fence.sync.aligned;
L335:         wgmma.mma_async { }, {%r80, ..}, ...; // uses %r81 directly after copy propagation
L336:         wgmma.commit_group.sync.aligned;
L337:         wgmma.wait_group.sync.aligned 1;
L338: 
L339:         bra $loop;
L340:         wgmma.wait_group.sync.aligned 0;
L341: Possible workarounds:
L342: 
L343:     1. Use `wgmma.wait_group.sync.aligned 0` to wait for all in-flight groups before the next `ldmatrix`.
L344: 
L345:     2. Use individual `ldmatrix.x1` loads directly into WGMMA input registers, which avoids the `mov` pattern that triggers the incorrect copy propagation.
L346: ## 2.6. Deprecated or Dropped Featurescite32† L347: ### 2.6.1. General CUDAcite33† L348: 
L349:   * CUDA 13.0 deprecates the following legacy vector types:
L350: 
L351:     * `double4`
L352: 
L353:     * `long4`
L354: 
L355:     * `ulong4`
L356: 
L357:     * `longlong4`
L358: 
L359:     * `ulonglong4`
L360: 
L361: These types are being replaced by new aligned variants:
L362: 
L363:     * `*_16a` and `*_32a` (e.g., `double4_16a`, `double4_32a`)
L364: 
L365: Deprecation warnings can be managed as follows:
L366: 
L367:     * Globally silenced by defining `__NV_NO_VECTOR_DEPRECATION_DIAG`
L368:     * Locally suppressed using the macro pair `__NV_SILENCE_HOST_DEPRECATION_BEGIN` / `__NV_SILENCE_HOST_DEPRECATION_END`
L369: 
L370: These legacy types are planned for removal in CUDA 14.0.
L371: 
L372:   * The CUDA installer for Windows no longer bundles the display driver. Users must install the display driver separately, either before or after installing the CUDA Toolkit.
L373:   * Multi-device launch APIs and related references for Cooperative Groups have been removed. These APIs were previously marked as deprecated in CUDA 12.x:
L374: 
L375:     * `cudaLaunchCooperativeKernelMultiDevice` has been removed from `cuda_runtime_api.h`.
L376: 
L377:     * The accompanying parameter struct `cudaLaunchParam` has been removed from `driver_types.h`.
L378: 
L379:     * `this_multi_grid` and `multi_grid_group` have been removed from `cooperative_groups.h`.
L380: 
L381:   * Changes to cudaDeviceProperties structure:
L382: In CUDA 13.0, several deprecated fields have been removed from the `cudaDeviceProperties` structure. To ensure forward compatibility, use the recommended replacement APIs listed below:
L383: 
L384: Removed Fields and Their Replacements
L385: Removed Field  | Replacement API
L386: --- | ---
L387: clockRate  | `cudaDeviceGetAttribute(cudaDevAttrClockRate)`
L388: deviceOverlap  | Use the `asyncEngineCount` field
L389: kernelExecTimeoutEnabled  | `cudaDeviceGetAttribute(cudaDevAttrKernelExecTimeout)`
L390: computeMode  | `cudaDeviceGetAttribute(cudaDevAttrComputeMode)`
L391: maxTexture1DLinear  | `cudaDeviceGetTexture1DLinearMaxWidth()`
L392: memoryClockRate  | `cudaDeviceGetAttribute(cudaDevAttrMemoryClockRate)`
L393: singleToDoublePrecisionPerfRatio  | `cudaDeviceGetAttribute(cudaDevAttrSingleToDoublePrecisionPerfRatio)`
L394: cooperativeMultiDeviceLaunch  | No replacement available
L395: Removed cudaDeviceAttr Types (No Replacement Available)
L396: 
L397:     * `cudaDevAttrCooperativeMultiDeviceLaunch`
L398: 
L399:     * `cudaDevAttrMaxTimelineSemaphoreInteropSupported`
L400: 
L401:   * The following legacy header files related to deprecated texture and surface references have been removed from the CUDA 13.0 runtime:
L402: 
L403:     * cuda_surface_types.h
L404: 
L405:     * cuda_texture_types.h
L406: 
L407:     * surface_functions.h
L408: 
L409:     * texture_fetch_functions.h
L410: ### 2.6.2. Deprecated Architecturescite34† L411: 
L412:   * Architecture support for Maxwell, Pascal, and Volta is considered feature-complete. Offline compilation and library support for these architectures have been removed in CUDA Toolkit 13.0 major version release. The use of CUDA Toolkits through the 12.x series to build applications for these architectures will continue to be supported, but newer toolkits will be unable to target these architectures.
L413: ### 2.6.3. Deprecated or Dropped Operating Systemscite35† L414: 
L415:   * Support for Ubuntu 20.04 has been dropped starting with this release. Users are advised to migrate to Ubuntu 22.04 LTS or later.
L416: 
L417: ### 2.6.4. Deprecated or Dropped CUDA Toolchainscite36† L418: 
L419: CUDA Tools
L420: 
L421:   * As of CUDA 13.1, support for Nsight Eclipse Edition plugins is deprecated, and will be dropped in a future CUDA release.
L422: # 3. CUDA Librariescite37† L423: 
L424: This section covers CUDA Libraries release notes for 13.x releases.
L425: 
L426: Note
L427: 
L428: Documentation will be updated to accurately reflect supported C++ standard libraries for CUDA Math Libraries.
L429: 
L430: ## 3.1. cuBLAS Librarycite38† L431: ### 3.1.1. cuBLAS: Release 13.2 Update 2cite39† --------------------------------------------------------------------------------
Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs | Ai2 (https://allenai.org/blog/olmocore3)
citeturn29550view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29549view2","id":33}); Total lines: 168
--------------------------------------------------------------------------------
Open-sourcing AstaBrief, the fast report-generation model in Asta | Ai2 (https://allenai.org/blog/astabrief)
citeturn29550view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: click({"ref_id":"turn29549view2","id":32}); Total lines: 197

