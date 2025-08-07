"""
parameters.py

Defines reusable and batch parameter sets for 1D Monte Carlo PDE simulations.
Each configuration is dynamically generated to ensure consistency across fields.

The main generator function yields the parameter dictionaries for each unique
combination of values across specified parameter lists. These dictionaries are
used by batch-run scripts to configure simulations.

All arrays (e.g. initial conditions) are generated dynamically based on the 
number of particles.
"""

import numpy as np
from itertools import product

def generate_batch_parameters():
    """
    Yields dictionaries representing simulation parameters.
    
    Each parameter set corresponds to a unique combination of:
    - delta_t (time step size)
    - diff_coe (diffusion coefficient)
    - alpha (reaction strength)
    - reaction_type (e.g 'linear')
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
            - 'initial_pos': np.ndarray of shape (num_particles, ),
            - 'reaction_type': str

    """
    param_grid = {
        "num_particles": [10000, 1000000],
        "delta_t": [0.001, 0.005],
        "diff_coe": [1.0, 2.0],
        "alpha": [0.5, 1.0, 1.5],
        "x0": [1.0, -2.0],
        "final_time": [0.01, 0.05, 0.10, 0.50, 1.00, 5.00, 10.00],
        "reaction_type": ["linear"],
        "advection_type": ["linear"]
    }

    keys = list(param_grid.keys())
    value_lists = [param_grid[k] for k in keys]

    for values in product(*value_lists):
        params = dict(zip(keys, values))
    
        num_steps = int(params["final_time"] / params["delta_t"])
        label = (
            f"T{params['final_time']:.1f}"
            f"_D{params['diff_coe']:.1f}"
            f"_alpha{params['alpha']:.1f}"
            f"_x0_{params['x0']:.1f}"
        )

        yield {
            "label": label, 
            "num_particles": params["num_particles"],
            "num_steps": num_steps,
            "delta_t": params["delta_t"],
            "diff_coe": params["diff_coe"],
            "alpha": params["alpha"],
            "reaction_type": params["reaction_type"],
            "advection_type": params["advection_type"],
            "final_time": params["final_time"],
            "initial_pos": np.ones(params["num_particles"]) * params["x0"]
        }