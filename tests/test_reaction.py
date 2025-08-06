"""
tests/test_reaction.py

Tests for the reaction function factory used in 1D Monte Carlo PDE simulations.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.reaction import get_reaction_function

def test_linear_reaction():
    alpha = 0.5
    R = get_reaction_function("linear", alpha=alpha)
    x = np.array([-2.0, 0.0, 2.0])
    expected = alpha * x
    assert np.allclose(R(x), expected), "Linear reaction function failed"

def test_invalid_reaction_type():
    try:
        _ = get_reaction_function("not_a_real_type")
    except ValueError as e:
        print("[PASS] Caught expected error for invalid type")
        return
    assert False, "Did not raise ValueError for invalid reaction type"

if __name__ == "__main__":
    test_linear_reaction()
    test_invalid_reaction_type()
    print("Reaction function test passed.")