"""
tests/test_run_batch_advection.py

Tests whether batch advection simulations run correctly with 
dynamic drift parameters.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.parameters import generate_batch_parameters
from src.diffusion import simulate_diffusion_source_realizations
from src.advection import get_velocity_function

def run_advection_simulation(params):
    # Build the drift function based on advection type
    params["advection_function"] = get_velocity_function(
        advection_type=params["advection_type"],
        alpha=params["alpha"]
    )

    return simulate_diffusion_source_realizations(
        num_steps=params["num_steps"],
        num_realizations=params["num_particles"],
        diff_coe=params["diff_coe"],
        delta_t = params["delta_t"],
        int_pos=params["initial_pos"],
        advection_function=params["advection_function"],
        reaction_function=None
    )

def test_batch_advection_loop():
    for i, params in enumerate(generate_batch_parameters()):
        print(f"[TEST] Running advection batch {i}: params['label']")
        positions, weights = run_advection_simulation(params)

        # --- Shape Checks ---
        assert isinstance(positions, np.ndarray)
        assert isinstance(weights, np.ndarray)
        assert positions.shape == (params["num_particles"], )
        assert weights.shape == (params["num_particles"], )
        
        # --- Value Check: Drift should affect position distribution ---
        assert not np.allclose(positions, params["initial_pos"],), "Drift should move particles"

        print(f"[PASS] {params['label']}")
        
if __name__ == "__main__":
    test_batch_advection_loop()
    print("Batch advection test completed successfully.")