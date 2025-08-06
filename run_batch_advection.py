"""
Main script for simulating 1D advection-diffusion using Monte Carlo methods.

This script runs a Monte Carlo simulation of a batch 1D advection-diffusion 
equation with divergence-dependent velocity fields.

Particles move stochastically and are influenced by a spatially dependent 
drift field. Path weights may be uniform or modified based on future 
extensions (e.g., source/sink terms).

Modules Used:
- `src.diffusion`: Core stepping logic for particle motion
- `src.advection`: Defines the drift velocity field u(x)
- `src.utils`: Functions for saving results and basic diagnostics

To configure the simulation:
- Import parameter sets from src/parameters.py

Outputs:
- Saves final positions and weights to the `data/` directory
- Results can be visualized using `notebooks/visualize_advection.ipynb`

Usage:
    python run_batch_advection.py
"""

# --- Imports ---
from src.parameters import generate_batch_parameters
from src.diffusion import simulate_diffusion_source_realizations  
from src.advection import get_velocity_function                 
# from src.utils import save_simulation_data                        

# --- Simulation Wrapper Function --
def run_advection_simulation(params):
    """
    Wrapper function to run a single advection-difusion simulation.

    Args:
        params (dict): Simulation configuration dictionary containing:
            - num_steps
            - num_particles
            - delta_t
            - diff_coe
            - initial_pos
            - advection_function
            - label (for output)

    Returns:
        tuple: (positions, weights)
    """
    return simulate_diffusion_source_realizations(
        num_steps=params["num_steps"],
        num_realizations=params["num_particles"],
        diff_coe=params["diff_coe"],
        delta_t=params["delta_t"],
        int_pos=params["initial_pos"],
        advection_function=params["advection_function"],
        reaction_function=None
    )

def main():
    for params in generate_batch_parameters():
        print(f"\nRunning Simulation: {params['label']}")

        # Construct appropriate advection function
        params["advection_function"] = get_velocity_function(
            advection_type= params["advection_type"],
            alpha = params["alpha"]
        )

        results = run_advection_simulation(params)

        # TODO: save results
        # save_simulation_data(*results, filename_prefix=f"advection_{params['label']}")
        print(f"Finished: {params['label']}")

# --- Run as script ---
if __name__ == "__main__":
    main()