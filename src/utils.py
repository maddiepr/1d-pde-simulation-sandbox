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

def plot_weighted_histogram(positions, weights=None, bins=100, range=None,
                            label=None, color=None, alpha=0.7, show=True,
                            exact_solution=None, exact_label="Exact", exact_color="black"):
    """
    Plots a weighted histogram and optionally overlays an exact solution.

    Args:
        positions (np.ndarray): Particle positions
        weights (np.ndarray or None): Path weights (same shape as position)
        bins (int): Number of histogram bins
        range (tuple or None): (min, max) range for histogram
        label (str): Legend label
        color (str): Histogram color
        alpha (float): Transparency level
        show (bool): Whether to call plt.show()
        exact_solution (callable or None): Function f(x) to overlay as exact PDF
        exact_label (str): Legend label for exact curve
        exact_color (str): Curve color

    Returns:
        counts (np.ndarray): Histogram bin heights
        edges (np.ndarray): Bin edges
    """
    counts, edges, _ = plt.hist(
        positions,
        bins=bins,
        range=range,
        weights=weights,
        density=True,
        label=label,
        color=color,
        alpha=alpha,
        edgecolor='black'
    )

    if exact_solution is not None:
        x_vals = 0.5 * (edges[:-1] + edges[1:])
        y_vals = exact_solution(x_vals)
        plt.plot(x_vals, y_vals, color=exact_color, label=exact_solution, linewidth=2)

    plt.xlabel("x")
    plt.ylabel("Estimated Density")
    plt.grid(True)

    if label or exact_solution:
        plt.legend()

    if show:
        plt.show()
    
    return counts, edges