"""
tests/test_run_batch_advection.py

Sanity test for batch advection runner using the real diffusion engine.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parameters import generate_batch_parameters
from src.diffusion import simulate_diffusion_source_realizations

def run_advection_simulation(params):
    return simulate_diffusion_source_realizations(
        num_steps=params["num_steps"],
        num_realizations=params["num_particles"],
        diff_coe=params["diff_coe"],
        delta_t = params["delta_t"],
        int_pos=params["initial_pos"],
        drift_function=None,
        reaction_function=None
    )

def test_batch_loop():
    for i, params in enumerate(generate_batch_parameters()):
        print(f"[TEST] Running batch {i}: params['label']")
        positions, weights = run_advection_simulation(params)
        assert positions.shape == (params["num_particles"], )
        assert weights.shape == (params["num_particles"], )
        print(f"[PASS] {params['label']}")
        
if __name__ == "__main__":
    test_batch_loop()
    print("Batch advection test completed successfully.")