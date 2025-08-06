"""
tests/test_run_batch_reaction.py

Basic flow test for the batch reaction driver.
Ensures that parameters load correctly and the main loop completes.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.parameters import generate_batch_parameters
from src.diffusion import simulate_diffusion_source_realizations
from src.reaction import get_reaction_function

def run_reaction_simulation(params):
    params["reaction_function"] = get_reaction_function(
        reaction_type = params["reaction_type"],
        alpha = params["alpha"]
    )
    return simulate_diffusion_source_realizations(
        num_steps = params["num_steps"],
        num_realizations = params["num_particles"],
        diff_coe = params["diff_coe"],
        delta_t = params["delta_t"],
        int_pos = params["initial_pos"],
        drift_function = None,
        reaction_function = params["reaction_function"]
    )

def test_batch_reaction_loop():
    for i, params in enumerate(generate_batch_parameters()):
        print(f"[TEST] Running batch {i}: params['label']")
        positions, weights = run_reaction_simulation(params)

        # --- Shape Checks ---
        assert isinstance(positions, np.ndarray)
        assert isinstance(weights, np.ndarray)
        assert positions.shape == (params["num_particles"], )
        assert weights.shape == (params["num_particles"], )
        
        # --- Value Check: Reaction should modify weights ---
        if params["reaction_type"] != "none":
            assert not np.allclose(weights, 1.0)

        print(f"[PASS] {params['label']}")
        
if __name__ == "__main__":
    test_batch_reaction_loop()
    print("Batch reaction test completed successfully.")
