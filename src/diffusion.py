"""
diffusion.py

This module contains the core logic for simulating 1D diffusion processes 
using Monte Carlo methods.

The main function simulates discrete particle stepping under stochastic 
motion, with optional support for reaction or advection terms passed as 
callable update rules.

Key Responsibilities:
- Initialize particle positions
- Perform Brownian stepping (with optional drift)
- Update particle weights step-by-step
- Return or save final positions and weights for statistical analysis

Typical Usage:
- Called by entry-point scripts (e.g. 'run_batch_reaction.py',
'run_batch_advection.py')
- Can be configured via direct parameters or external config modules

Planned Extensions:
- Support for spatially dependent diffusion coefficients D(x)
- Optional boundary handing (reflecting, absorbing)
- Vectorized stepping for performance optimization
"""

import numpy as np

def simulate_diffusion_source_realizations(
        num_steps,
        num_realizations,
        diff_coe,
        delta_t,
        int_pos,
        advection_function=None,
        reaction_function=None
):
    """
    Simulates diffusion of particles with optional drift or reaction.

    Args:
        num_steps: int
        num_realizations: int
        diff_coe: float
        delta_t: float
        int_pos: np.ndaray
        advection_function: callable
        reaction_function: callable

    Returns:
        positions (np.ndarray): Final particle positions
        weights (np.ndarray): Final path weights
    """

    # --- Initialize positions and weights ---
    positions = np.copy(int_pos)            # shape: (num_realizations, )
    weights = np.ones(num_realizations)     # all paths start with weight 1

    # --- Precompute constants ---
    sqrt_2Ddt = np.sqrt(2 * diff_coe * delta_t)

    # --- Time stepping loop ---
    for step in range(num_steps):
        
        # --- Apply advection term ---
        if advection_function is not None:           
            drift = advection_function(positions)   # shape: (num_realizations, )
        else:
            drift = 0.0                         # scalar drift = 0 if none provided

        # --- Brownian step + drift step ---
        noise = np.random.normal(loc=0.0, scale=1.0, size=num_realizations)
        delta_x = drift*delta_t + sqrt_2Ddt * noise

        # --- Update positions ---
        positions += delta_x

        # --- Apply reaction weight updates ---
        if reaction_function is not None:
            reaction_rate = reaction_function(positions)    # shape: (num_realizations, )
            weights *= np.exp(-reaction_rate * delta_t)     # multiplicative weight decay

    return positions, weights