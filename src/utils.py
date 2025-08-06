"""
utils.py

This module provides general-purpose utility functions to support
simulation workflows, including data saving, histogram building,
statistical analysis, and basic plotting.

These utilities are used by both reaction and advection simulation
pipelines and are designed to keep the core logic in 'src.diffusion'
clean and modular.

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

import os
import numpy as np

def save_simulation_data(positions, weights, label, sim_type, base_dir="data"):
    """
    Saves simulation data to organized directory structure.

    Args:
        positions (np.ndarray): Final particle positions
        weights (np.ndarray): Final path weights
        label (str): Parameter-dependent label (folder name)
        sim_type (str): Either 'reaction' or 'advection'
        base_dir (str): Top-level output directory

    Files saved:
        - {out_dir}/{prefix}_positions.npy
        - {out_dir}/{prefix}_weights.npy
    """
    out_dir = os.path.join(base_dir, sim_type, label)
    os.makedirs(out_dir, exist_ok=True)

    np.save(os.path.join(out_dir, "positions.npy"), positions)
    np.save(os.path.join(out_dir, "weights.npy"), weights)

    print(f"[INFO] Saved simulation to: {out_dir}")