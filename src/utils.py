"""
utils.py

This module provides general-purpose utility functions to support
simulation workflows, including data loading, saving, and I/O
helpers for both reaction and advection simulations.

These utilities are used by simulation drivers and notebooks, and
are designed to keep core numerical logic clean and modular.

Key Responsibilities:
- Save and load particle positions and weights
- Organize simulation output structure
- Handle parameter configuration and file naming

Typical Usage:
- Called from 'run_*.py' scripts after simulations complete
- Called from Jupyter notebooks for visualization
- Used in notebooks to load simulation data for analysis

Planned Extensions:
- Add support for alternative file formats (e.g., JSON, HDF5)
- Add utilities for parameter parsing from folder names
"""

import os
import re
import numpy as np
import matplotlib.pyplot as plt

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

def load_simulation_data(folder):
    """
    Loads simulation output (positions and weights) from a given folder.

    Args:
        folder (str): Path to the simulation output directory
    
    Returns:
        tuple: (positions, weights) as np.ndarrays
    """
    pos_path = os.path.join(folder, "positions.npy")
    wgt_path = os.path.join(folder, "weights.npy")

    if not os.path.exists(pos_path) or not os.path.exists(wgt_path):
        raise FileNotFoundError(f"Missing simulation files in: {folder}")
    
    positions = np.load(pos_path)
    weights = np.load(wgt_path)

    print(f"[INFO] Loaded data from: {folder}")
    return positions, weights

def parse_parameters_from_foldername(foldername):
    """
    Extracts parameters T, D (kappa), alpha, x0 from a folder name of the form:
    T1.0_D1.0_alpha1.0_x0_1.0

    Returns:
        dict: { 'T': float, 'D': float, 'alpha': float, 'x0': float)}
    """

    pattern = r"^T(?P<T>[\d\.]+)_D(?P<D>[\d\.]+)_alpha(?P<alpha>[\d\.]+)_x0_(?P<x0>-?[\d\.]+)$"
    match = re.match(pattern, foldername)
    if not match:
        raise ValueError(f"Folder name format not recognized: {foldername}")
    
    return{
        'T': float(match.group("T")),
        'D': float(match.group("D")),
        'alpha': float(match.group("alpha")),
        'x0': float(match.group('x0'))
    }