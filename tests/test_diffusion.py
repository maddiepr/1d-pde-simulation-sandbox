"""
tests/test_diffusion.py

Basic test for simulate_diffusion_source_realizations in diffusion.py
This verifies shape and sanity of the output with no drift or reaction.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.diffusion import simulate_diffusion_source_realizations

def test_diffusion_no_drift_or_reaction():
    print("\n[TEST] Running diffusion with no drift or reaction...")

    num_particles = 1000
    num_steps = 500
    delta_t = 0.01
    diff_coe = 1.0
    initial_pos = np.zeros(num_particles)

    positions, weights = simulate_diffusion_source_realizations(
        num_steps=num_steps,
        num_realizations=num_particles,
        diff_coe=diff_coe,
        delta_t=delta_t,
        int_pos=initial_pos,
        drift_function=None,
        reaction_function=None
    )

    assert isinstance(positions, np.ndarray)
    assert isinstance(weights, np.ndarray)
    assert positions.shape == (num_particles, )
    assert weights.shape == (num_particles, )

    # --- Sanity Printouts ---
    print(f" Final position mean: {np.mean(positions):.4f}")
    print(f" Final position std: {np.std(positions):.4f}")
    print(f" Final weight mean: {np.mean(weights):.4f}")
    print(f" All weights = 1?: {np.allclose(weights, 1.0)}")

    print("[PASS] Diffusion test completed successfully.")

if __name__ == "__main__":
    test_diffusion_no_drift_or_reaction()