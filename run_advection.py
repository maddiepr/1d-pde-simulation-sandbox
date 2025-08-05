"""
Main script for simulating 1D advection-diffusion using Monte Carlo methods.

This script runs a Monte Carlo simulation of a 1D advection-diffusion equation with divergence-dependent velocity fields.

Particles move stochastically and are influenced by a spatially dependent drift field. Path weights may be uniform or modified based on future extensions (e.g., source/sink terms).

Modules Used:
- `src.diffusion`: Core stepping logic for particle motion
- `src.advection`: Defines the drift velocity field u(x)
- `src.utils`: Functions for saving results and basic diagnostics

To configure the simulation:
- Modify parameter values directly in this script or import from an external config

Outputs:
- Saves final positions and weights to the `data/` directory
- Results can be visualized using `notebooks/visualize_advection.ipynb`

Usage:
    python run_advection.py
"""
