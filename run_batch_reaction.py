"""
Main script for simulating 1D reaction-diffusion using Monte Carlo methods.

This script runs a Monte Carlo simulation of a 1D reaction-diffusion equation using discrete particle stepping

Particles undergo stochastic diffusion with path weights updated according to a spatially dependent reaction term.
The simulation outputs the final particle positions and associated weights for statistical analysis and comparison to exact solutions.

Modules Used:
- 'src.diffusion': Core stepping logic for particle motion
- 'src.reaction': Defines the weight update rule based on the reaction field
- 'src.utils': Functions for saving results and basic diagnostics

To configure the simulation:
- Modify parameter values directly in this script or import from an external config

Outputs:
- Saves final positions and weights to the 'data/' directory
- Results can be visualized using 'notebooks/visualize_reaction.ipynb'

Usage:
    python run_reaction.py
"""