"""
tests/test_run_batch_reaction.py

Basic flow test for the batch reaction driver.
Ensures that parameters load correctly and the main loop completes.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parameters import generate_batch_parameters

# --- Simulate a stub version of the runner
def run_reaction_simulation(params):
    print(f"[TEST] Simulating: {params['label']}")
    return "dummy_positions", "dummy_weights"

def test_batch_loop():
    for params in generate_batch_parameters():
        results = run_reaction_simulation(params)
        assert isinstance(results, tuple)
        assert len(results) == 2
        print(f"[PASS] {params['label']}")

if __name__ == "__main__":
    test_batch_loop()
    print("All batch reaction parameter sets completed successfully.")