"""
src package

This package contains the core modules for simulating 1D PDEs using Monte Carlo methods.
Each module implements specific terms or utilities used by the entry-point scripts.

Modules:
- diffusion.py: Base logic for particle stepping and weight evolution
- reaction.py: Functions defining reaction terms
- advection.py: Functions for drift/advection fields
- utils.py: Tools for saving data, visualizing results, and histogram generation
"""

from src.utils import save_simulation_data, load_simulation_data, plot_weighted_histogram
from src.diffusion import simulate_diffusion_source_realizations
from src.reaction import get_reaction_function
from src.advection import get_velocity_function

__all__ = [
    "save_simulation_data",
    "load_simulation_data",
    "plot_weighted_histogram",
    "simulate_diffusion_source_realizations",
    "get_reaction_function",
    "get_velocity_function"
]