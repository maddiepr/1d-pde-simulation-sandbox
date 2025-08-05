"""
utils.py

This module provides general-purpose utility functions to support simulation workflows,
including data saving, histogram building, statistical analysis, and basic plotting.

These utilities are used by both reaction and advection simulation pipelines and are
designed to keep the core logic in 'src.diffusion' clean and modular.

Key Responsibilities:
- Save particle positions and weights to disk
- Generate histograms and normalized density estimates
- Provide plotting functions for visualizing simulation results
- Load saved data for downstream analysis

Typical Usage:
- Called from 'run_*.py' scripts after a simulation completes
- Used in notebooks for post-processing and comparion to analytical results

Planned Extensions:
- Add more robust file I/O options (e.g. JSON, CSV, HDF5)
- Add automated error metrics and comparison tools
"""