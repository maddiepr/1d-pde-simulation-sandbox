"""
plotting.py

This module provides all visualization and plotting utilities for
the 1D PDE Monte Carlo simulations, including weighted histograms,
comparison plots with exact solutions, and batch visualization tools.

By separating plotting logic from utilities and core simulation code,
this module supports clean reuse in both notebooks and automation scripts.

Key Responsibilities:
- Generate weighted histograms of final particle distributions
- Overlay exact solutions for comparison
- Save plots to disk for documentation or review
- Support batch plotting of all simulation runs in a directory

Typical Usage:
- Called from Jupyter notebooks during exploratory analysis
- Used in batch jobs to automatically generate plots after runs

Planned Extensions:
- Add time-evolution plots for intermediate snapshots
- Add support for saving in multiple formats (e.g., PDF, SVG)
- Add 2D/heatmap visualizations for future simulations
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from src.utils import parse_parameters_from_foldername
from src.exact_solutions import advection_solution, reaction_solution

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
        plt.plot(x_vals, y_vals, color=exact_color, label=exact_label, linewidth=2)

    plt.xlabel("x")
    plt.ylabel("Estimated Density")
    plt.grid(True)

    if label or exact_solution:
        plt.legend()
    
    return counts, edges

def plot_and_save_all_histograms(
    base_dir,
    output_dir,
    title_prefix="",
    show_one=True,
    bins=100,
    range=None,
    exact_solution=None,
    exact_label="Exact",
    exact_color="black",
    histogram_color=None
):
    """
    Loops through simulation folders and saves weighted histograms to disk.
    Displays only the first one by default.

    Args:
        base_dir (Path): Directory containing simulation subfolders
        output_dir (Path): Where to save the histogram plots
        title_prefix (str): Prefix to prepend to plot titles
        show_one (bool): Whether to display the first plot
        bins (int): Number of histogram bins
        range (tuple): (min, max) x-range for histogram
        exact_solution (callable): Function to overlay on histogram
        exact_label (str): Label for exact curve
        exact_color (str): Color for exact curve
        histogram_color (str): Color for histogram
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    available_runs = sorted([f for f in base_dir.iterdir() if f.is_dir()])

    for i, run_path in enumerate(available_runs):
        print(f"Processing: {run_path.name}")
        positions = np.load(run_path/"positions.npy")
        weights = np.load(run_path/"weights.npy")

        # ---Parse parameters from folder name ---
        params = parse_parameters_from_foldername(run_path.name)
        T_val = params['T']
        D_val = params['D']
        alpha_val = params['alpha']

        # --- Define exact solution for this run ---
        if exact_solution == "reaction":
            exact_fn = lambda x: reaction_solution(x, t=T_val, alpha=alpha_val, kappa=D_val)
        elif exact_solution == "advection":
            exact_fn = lambda x: advection_solution(x, t=T_val, alpha=alpha_val, kappa=D_val)
        else:
            exact_fn = None     # not comparing to exact solution

        # --- Plot and Save ---
        title = f"{title_prefix}{run_path.name}"
        save_path = output_dir/f"{run_path.name}.png"

        plt.figure(figsize=(8, 5))
        plot_weighted_histogram(
            positions=positions,
            weights=weights,
            bins=bins,
            range=range,
            label="Simulation",
            color=histogram_color,
            show=(i == 0 and show_one),
            exact_solution=exact_fn,
            exact_label=exact_label,
            exact_color=exact_color
        )

        plt.title(title)
        plt.tight_layout()
        plt.savefig(save_path)
        print(f"Saved to: {save_path}")
        plt.close()
    