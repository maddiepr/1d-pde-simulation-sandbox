import numpy as np

'''
Defines sizes and x-val end points of histogram based on simulation parameters
    Variables:
        B: number of desired bins
    Parameters:
        diff_coe: float
            Diffusion coefficient
        num_steps: int
            Number of steps in simulation
        delta_t: float
            Size of time step
        num_bins: int
            Number of desired bins for histogram
    Returns:
        spatial_bins: [N + 1, ]
            Widths for each bin for histogram
'''

def define_spatial_bins(diff_coe, 
                        num_steps, 
                        delta_t, 
                        num_bins):

    # Define Final Time
    time_final = delta_t * num_steps 

    # Estimate the spread of histogram
    spread_estimate = np.sqrt(2 * diff_coe * time_final) 

    # Define max and min for histogram
    domain_min = - spread_estimate * 3 
    domain_max = spread_estimate * 3 

    # Define end points of bins
    spatial_bins = np.linspace(domain_min, domain_max, num_bins + 1) # [B + 1, ]

    return spatial_bins # [B + 1, ]