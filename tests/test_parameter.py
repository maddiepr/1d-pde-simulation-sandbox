"""
tests/test_parameters.py

Basic sanity tests for parameter generation used in batch simulations
These ensure that all parameter sets are consistent and valid before running simulation.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.parameters import generate_batch_parameters

def test_generate_parameters():
    for i, p in enumerate(generate_batch_parameters()):
        print(f"Testing parameter set {i}: {p['label']}")

        # --- Structural Checks ---
        assert isinstance(p["label"], str)
        assert isinstance(p["num_particles"], int)
        assert isinstance(p["num_steps"], int)
        assert isinstance(p["delta_t"], float)
        assert isinstance(p["diff_coe"], float)
        assert isinstance(p["final_time"], float)
        assert isinstance(p["reaction_type"], str)
        assert isinstance(p["advection_type"], str)
        assert isinstance(p["alpha"], float)

        # --- Array Checks ---
        assert isinstance(p["initial_pos"], np.ndarray)
        assert len(p["initial_pos"]) == p["num_particles"]

        # --- Value Checks ---
        assert p["num_steps"] > 0
        assert p["delta_t"] > 0
        assert p["diff_coe"] > 0

    print("All parameter sets passed the basic validation test.")

if __name__ == "__main__":
    test_generate_parameters()