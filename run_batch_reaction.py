"""
Main script for simulating 1D reaction-diffusion using Monte Carlo methods.

This script runs a Monte Carlo simulation of a 1D reaction-diffusion equation 
using discrete particle stepping.

Particles undergo stochastic diffusion with path weights updated according to 
a spatially dependent reaction term.
The simulation outputs the final particle positions and associated weights for
statistical analysis and comparison to exact solutions.

Modules Used:
- 'src.diffusion': Core stepping logic for particle motion
- 'src.reaction': Defines the weight update rule based on the reaction field
- 'src.utils': Functions for saving results and basic diagnostics

To configure the simulation:
- Import parameter sets from src.parameters.py

Outputs:
- Saves final positions and weights to the 'data/' directory
- Results can be visualized using 'notebooks/visualize_reaction.ipynb'

Usage:
    python run_batch_reaction.py
"""

# --- Imports ---
from src.parameters import generate_batch_parameters
from src.diffusion import simulate_diffusion_source_realizations
from src.reaction import get_reaction_function 
# from src.utils import save_simulation_data

# --- Simulation Wrapper Function ---
def run_reaction_simulation(params):
    """
    Runs a single reaction-diffusion simulation using Monte Carlo methods.

    Args:
        params (dict): Simulation configuration dictionary containing:
            - num_steps: int
            - num_particles: int
            - delta_t: int
            - diff_coe: float
            - alpha: float
            - initial_pos: np.ndarray
            - reaction_function: callable
            - label: str

    Returns:
        tuple: (positions, weights)
    """
    return simulate_diffusion_source_realizations(
        num_steps=params["num_steps"],
        num_realizations=params["num_particles"],
        diff_coe=params["diff_coe"],
        delta_t=params["delta_t"],
        int_pos=params["initial_pos"],
        drift_function=None,     
        reaction_function=params["reaction_function"]
    )

# --- Batch Execution Loop ---
def main():
    for params in generate_batch_parameters():
        print(f"\nRunning Simulation: {params['label']}")

        # Construct appropriate reaction function based on type
        params["reaction_function"] = get_reaction_function(
            reaction_type= params["reaction_type"],
            alpha = params["alpha"]
        )

        results = run_reaction_simulation(params)

        # TODO: save results
        # save_simulation_data(*results, filename_prefix=f"reaction_{params['label']}")
        print(f"Finished: {params['label']}")

# --- Run as script ---
if __name__ == "__main__":
    main()