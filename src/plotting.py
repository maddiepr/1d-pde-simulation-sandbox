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
import seaborn as sns
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
        exact_solution (callable or None): Exact solution to overlay.
            If 'reaction' or 'advection' is passed, the overlay is computed
            assuming a **linear** reaction or advection term. No exact solution
            is available for quadratic or Gaussian reaction terms.
        exact_label (str): Legend label for exact curve
        exact_color (str): Curve color

    Returns:
        counts (np.ndarray): Histogram bin heights
        edges (np.ndarray): Bin edges
    """
    # --- Compute histogram
    counts, edges = np.histogram(
        positions,
        bins=bins,
        range=range,
        weights=weights,
        density=False  # ← disable density so we can normalize manually
    )

    # --- Manual normalization
    bin_width = edges[1] - edges[0]
    num_realizations = np.sum(weights)
    normalized_density = counts / (bin_width * num_realizations)
    bin_centers = 0.5 * (edges[:-1] + edges[1:])

    # --- Plot normalized histogram
    plt.bar(bin_centers, normalized_density, width=bin_width,
            edgecolor='black', alpha=alpha, color=color, label=label)

    # --- Compute Simulation Stats ---
    mean = np.average(positions, weights=weights)
    variance = np.average((positions - mean)**2, weights=weights)
    std_dev = np.sqrt(variance)

    stat_text = f"Sim mean = {mean:.2f}, σ = {std_dev:.2f}"

    if exact_solution is not None:
        # --- Evaluate exact solution ---
        x_vals = 0.5 * (edges[:-1] + edges[1:])
        y_vals = exact_solution(x_vals)

        # --- Compute bin centers and normalized density for MSE ---
        bin_centers = x_vals
        dx = x_vals[1] - x_vals[0]
        area = np.sum(y_vals) * dx

        if area > 0 and np.isfinite(area):
            y_vals_norm = y_vals / area

            # Compute exact stats
            mean_exact = np.sum(x_vals * y_vals_norm) * dx
            var_exact = np.sum((x_vals - mean_exact)**2 * y_vals_norm) * dx
            std_exact = np.sqrt(var_exact)

            # Interpolate simulation density (already normalized by `density=True`)
            y_sim, _ = np.histogram(positions, bins=edges, weights=weights, density=True)
            y_sim_interp = np.interp(x_vals, bin_centers, y_sim)

            # Compute MSE
            mse = np.mean((y_sim_interp - y_vals_norm)**2)

            # Update annotation
            stat_text += (
                f"\nExact: μ = {mean_exact:.2f}, σ = {std_exact:.2f}"
                f"\nMSE = {mse:.2e}"
            )

            # Plot normalized exact curve
            plt.plot(x_vals, y_vals_norm, color=exact_color, label=exact_label, linewidth=2)

        else:
        # Skip plotting exact solution if invalid
            print("Exact solution not plotted: zero or invalid area.")

    # --- Annotate ---
    plt.annotate(
        stat_text,
        xy=(0.02, 0.98),
        xycoords="axes fraction",
        fontsize=10,
        ha="left",   # was `hs`, which is invalid
        va="top",    # was `vs`, which is invalid
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray")
    )

    # --- Labels and Legend ---
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
        positions = np.load(run_path/"positions.npy")
        weights = np.load(run_path/"weights.npy")

        # ---Parse parameters from folder name ---
        params = parse_parameters_from_foldername(run_path.name)
        T_val = params['T']
        D_val = params['D']
        alpha_val = params['alpha']

        # --- Define exact solution for this run ---
        if exact_solution == "reaction":
            exact_fn = lambda x: reaction_solution(x, t=T_val, alpha=alpha_val, kappa=D_val, x0=params['x0'])
        elif exact_solution == "advection":
            exact_fn = lambda x: advection_solution(x, t=T_val, alpha=alpha_val, kappa=D_val, x0=params['x0'])
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
        plt.close()
    
def plot_mse_vs_param(
        metrics_df,
        param_to_vary,
        fixed_params,
        title_prefix="",
        figsize=(7, 4)
):
    """
    Plot MSE vs one parameter, fixing others.

    Args:
        metrics_df (pd.DataFrame): DataFrame containing stats for each run
        param_to_vary (str): One of 'T', 'D', 'alpha', 'x0'
        fixed_params (dict): e.g., {'alpha': 1.0, 'D'= 1.0, 'x0':0.0}
        title_prefix (str): Optional title prefix
        figsize (tuple): Figure size
    """
    # --- Filter based on fixed params ---
    query = "&".join([f"{k} == {v}" for k, v in fixed_params.items()])
    subset = metrics_df.query(query)

    if subset.empty:
        print("No data matches the given fixed parameters.")
    
    # --- Sort and plot ---
    subset = subset.sort_values(param_to_vary)
    plt.figure(figsize=figsize)
    sns.lineplot(data=subset, x=param_to_vary, y="MSE", marker="o")

    # --- Title and Labels ---
    fixed_str = ",".join([f"{k}={v}" for k, v in fixed_params.items()])
    plt.title(f"{title_prefix}MSE vs {param_to_vary} ({fixed_str})")
    plt.xlabel(param_to_vary)
    plt.ylabel("Mean Squared Error (MSE)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_mse_heatmap(
        metrics_df,
        param_x,
        param_y,
        fixed_params={},
        title_prefix="",
        figsize=(8,6)
):
    """
    Plot a heatmap showing MSE over two varying parameters.

    Args:
        metrics_df (pd.DataFrame): DataFrame of metrics
        param_x (str): Parameter on x-axis (e.g. 'T')
        param_y (str): Parameter on y-axis (e.g. 'alpha')
        fixed_params (dict): Parameters to fix, e.g. {'x0': 1.0}
        title_prefix (str): Optional title prefix
        figsize (tuple): Figure size
    """
    # --- Filter by fixed params ---
    query = "&".join([f"{k}=={v}" for k, v in fixed_params.items()])
    if query:
        subset = metrics_df.query(query)
    else:
        subset = metrics_df.copy()
    
    if subset.empty:
        print("No data matches the given fixed parameters.")
        return
    
    # --- Pivot for heatmap ---
    pivot = subset.pivot_table(index=param_y, columns=param_x, values="MSE")

    # --- Plot ---
    plt.figure(figsize=figsize)
    sns.heatmap(pivot, annot=True, fmt=".1e", cmap="mako", cbar_kws={"label": "MSE"})
    fixed_str = ", ".join([f"{k}={v}" for k, v in fixed_params.items()])
    suffix = f" ({fixed_str})" if fixed_str else ""
    plt.title(f"{title_prefix}MSE Heatmap: {param_y} vs {param_x}{suffix}")
    plt.xlabel(param_x)
    plt.ylabel(param_y)
    plt.tight_layout()
    plt.show()