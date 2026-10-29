"""
Core GPU energy measurement functionality.
"""
import os
import time
from typing import Optional, Callable, Any, List
from contextlib import contextmanager
import torch
from pynvml import *


class GPUEnergyMeter:
    """
    A class for measuring GPU energy consumption using NVIDIA Management Library.
    
    Attributes:
        device_index (int): CUDA device index to measure
        handle: NVML device handle
        initialized (bool): Whether NVML has been initialized
    
    Example:
        >>> meter = GPUEnergyMeter(device_index=0)
        >>> with meter.measure() as measurement:
        ...     # Your GPU code here
        ...     model(inputs)
        >>> print(f"Energy used: {measurement.energy_mj} mJ")
    """
    
    def __init__(self, device_index: int = 0, set_visible_devices: bool = True):
        """
        Initialize the GPU energy meter.
        
        Args:
            device_index: CUDA device index to monitor (default: 0)
            set_visible_devices: Whether to set CUDA_VISIBLE_DEVICES environment variable
        """
        self.device_index = device_index
        self.initialized = False
        
        if set_visible_devices:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(device_index)
        
        self._initialize_nvml()
    
    def _initialize_nvml(self):
        """Initialize NVML library and get device handle."""
        if not self.initialized:
            try:
                nvmlInit()
                self.handle = nvmlDeviceGetHandleByIndex(self.device_index)
                self.initialized = True
            except NVMLError as err:
                raise RuntimeError(f"Failed to initialize NVML: {err}")
    
    def get_energy_mj(self) -> float:
        """
        Get total GPU energy consumption in millijoules since boot.
        
        Returns:
            Total energy in millijoules
        """
        if not self.initialized:
            raise RuntimeError("NVML not initialized. Call _initialize_nvml() first.")
        
        try:
            return nvmlDeviceGetTotalEnergyConsumption(self.handle)
        except NVMLError as err:
            print(f"NVML Error: {err}")
            return 0.0
    
    @contextmanager
    def measure(self):
        """
        Context manager for measuring energy consumption of a code block.
        
        Yields:
            Measurement object with energy_mj attribute
            
        Example:
            >>> with meter.measure() as m:
            ...     model(inputs)
            >>> print(m.energy_mj)
        """
        class Measurement:
            def __init__(self):
                self.energy_mj = 0.0
        
        measurement = Measurement()
        start_energy = self.get_energy_mj()
        
        try:
            yield measurement
        finally:
            end_energy = self.get_energy_mj()
            measurement.energy_mj = end_energy - start_energy
    
    def measure_function(
        self,
        func: Callable,
        *args,
        num_trials: int = 1,
        repeat_count: int = 1,
        warmup: bool = True,
        sleep_between_trials: float = 0.0,
        **kwargs
    ) -> dict:
        """
        Measure energy consumption of a function over multiple trials.
        
        Args:
            func: Function to measure
            *args: Positional arguments to pass to func
            num_trials: Number of measurement trials
            repeat_count: Number of times to repeat the function in each trial
            warmup: Whether to run a warmup iteration before measurements
            sleep_between_trials: Seconds to sleep between trials
            **kwargs: Keyword arguments to pass to func
            
        Returns:
            Dictionary containing energy statistics
            
        Example:
            >>> def forward_pass():
            ...     model(inputs)
            >>> results = meter.measure_function(forward_pass, num_trials=10, repeat_count=100)
            >>> print(f"Mean energy: {results['mean_mj']} mJ")
        """
        if warmup:
            # Run once to warm up GPU
            with torch.no_grad():
                func(*args, **kwargs)
            if torch.cuda.is_available():
                torch.cuda.synchronize()
            time.sleep(1)
        
        energy_usages = []
        
        for trial in range(num_trials):
            if sleep_between_trials > 0 and trial > 0:
                time.sleep(sleep_between_trials)
            
            start_energy = self.get_energy_mj()
            
            # Run the function repeat_count times
            for _ in range(repeat_count):
                func(*args, **kwargs)
            
            # Ensure GPU operations are complete
            if torch.cuda.is_available():
                torch.cuda.synchronize()
            
            end_energy = self.get_energy_mj()
            
            # Calculate per-iteration energy
            energy_per_iter = (end_energy - start_energy) / repeat_count
            energy_usages.append(energy_per_iter)
            
            print(f"Trial {trial+1}/{num_trials}: {energy_per_iter:.4f} mJ")
        
        # Calculate statistics
        from .utils import calculate_energy_stats
        stats = calculate_energy_stats(energy_usages)
        
        return stats
    
    def shutdown(self):
        """Shutdown NVML library."""
        if self.initialized:
            nvmlShutdown()
            self.initialized = False
    
    def __enter__(self):
        """Support for using GPUEnergyMeter as a context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cleanup when exiting context manager."""
        self.shutdown()
        return False
    
    def __del__(self):
        """Cleanup when object is deleted."""
        try:
            self.shutdown()
        except:
            pass


@contextmanager
def measure_energy(device_index: int = 0):
    """
    Simple context manager for quick energy measurements.
    
    Args:
        device_index: CUDA device index to monitor
        
    Yields:
        Measurement object with energy_mj attribute
        
    Example:
        >>> with measure_energy() as m:
        ...     model(inputs)
        >>> print(f"Energy: {m.energy_mj} mJ")
    """
    meter = GPUEnergyMeter(device_index=device_index, set_visible_devices=False)
    try:
        with meter.measure() as measurement:
            yield measurement
    finally:
        meter.shutdown()
