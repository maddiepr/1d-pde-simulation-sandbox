import numpy as np
import random
from Save_values import save_values

'''
Simulates the diffusion drift equation, stores end positions
    Variables:
        R: Number of realizations
    Parameters:
        num_steps: int
            Desired amount of time steps
        diff_coe: float
            Coefficient for diffusion term
        alpha: float
            Coefficient for drift term
        delta_t: float
            Size of time step
        int_pos: [R, ] float
            Starting positions of each realization
        seed: int
            Default = no seed
            Set for reproducibility
    Returns:
        positions: [R, ] float
            Final position of particle
'''

def simulate_diffusion_source_realizations(num_steps, 
                             num_realizations, 
                             diff_coe, 
                             delta_t, 
                             int_pos,
                             intial_T, 
                             seed=None):
    
    # Sets seed if desired
    random.seed(seed)

    # Intialize starting position
    positions = int_pos # [R, ]

    # Initialize solution array
    T_vals = intial_T # [R, ]

    for step in range(1, num_steps):
        
        # Find diffusion term
        random_step = np.sqrt(2 * diff_coe * delta_t) * \
                            np.random.normal(0, 1, num_realizations) # [R, ]
        
        # Update the position
        positions += random_step   # [R, ]

        # Update T for each step
        T_vals = T_vals + positions * T_vals * delta_t 

    save_values(positions, "Final_Positions")
    save_values(T_vals, "Final_T_values")
    
    # Return final position
    return None