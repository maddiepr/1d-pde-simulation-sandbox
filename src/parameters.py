"""
parameters.py

Defines reusable and batch parameter sets for 1D Monte Carlo PDE simulations.
Each configuration is dynamically generated to ensure consistency across fields.
"""

import numpy as np
from itertools import product

def generate_batch_parameters():
    """
    Yields dictionaries for each unique parameter combination.
    Uses a full Cartesian product across the specified parameter list.
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