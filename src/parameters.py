"""
parameters.py

Defines reusable and batch parameter sets for 1D Monte Carlo PDE simulations.
Each configuration is dynamically generated to ensure consistency across fields.

The main generator function yields the parameter dictionaries for each unique
combination of values across specified parameter lists. These dictionaries are
used by batch-run scripts to configure simulations.

All array (e.g. initial conditions) are generated dynamically based on the 
number of particles.
"""

import numpy as np
from itertools import product

def generate_batch_parameters():
    """
    Yields dictionaries representing simulation parameters.
    
    Each parameter set corresponding to a unique combination of:
    - delta_t (time step size)
    - diff_coe (diffusion coefficient)
    - x0 (starting position)
    - final_time (used to calculate num_steps)

    Returns:
        dict: A parameter set with fields:
            - 'label': A string label for use in output filenames
            - 'num_particles': int
            - 'num_steps': int (computed from final_time / delta_t)
            - 'delta_t': float
            - 'diff_coe': float
            - 'final_time': float
            - 'initial_pos': np.ndarray of shape (num_particles, )

    """
    num_particles_list = [10000]
    delta_t_list = [0.01, 0.05]
    diff_coe_list = [1.0, 2.0]
    start_pos_list = [0.0, -2.0]
    final_time_list = [1.0]

    for delta_t, diff_coe, num_particles, x0, final_time in product(
        delta_t_list, diff_coe_list, num_particles_list, start_pos_list, final_time_list
    ):
        num_steps = int(final_time / delta_t)
        label = f"T_{final_time:.1f}__D_{diff_coe:.1f}__dt_{delta_t:.3f}__x0_{x0:.1f}"

        yield {
            "label": label, 
            "num_particles": num_particles,
            "num_steps": num_steps,
            "delta_t": delta_t,
            "diff_coe": diff_coe,
            "final_time": final_time,
            "initial_pos": np.ones(num_particles) * x0
        }