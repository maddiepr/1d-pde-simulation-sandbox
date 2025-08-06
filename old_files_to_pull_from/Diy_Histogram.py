import numpy as np
import random
from Save_values import save_values

'''
Creates histogram of scaled values
    Variables:
        R = Number of realizations
        N = Number of steps
        B = Number of bins
    Parameters:
        num_steps: int
            Number of time steps 
        T: int
            Final time the sim is going to
        num_bins: int
            Number of desired bins for histogram
    Returns: 
        counts: [B, ]
            Number of realizations in each histogram bin
        bin_edges: [B + 1, ]
            x-values of end points of bins
'''


def hist_diy(num_bins, final_positions, num_real, T ):

    # Find bounds for histogram
    max_pos = max(final_positions) # float
    min_pos = min(final_positions) # float

    # Find bin sizes
    delta_l = (max_pos - min_pos) / num_bins # float
    bin_edges = np.linspace(min_pos, max_pos, num_bins + 1) # [(x, y ) ]

    # Initialize count
    count = np.zeros(num_bins) # [B, ]

    for i in range(1, num_bins):

        for j in range(0, num_real):

            if (min_pos + delta_l*(i-1) <= final_positions[j]) and (final_positions[j] < min_pos + delta_l * (i) ) :
                
                count[i] = count[i]  +  T[j]

    # Save count values to a .txt file            
    save_values(count, "Count_values")
    
    return count, bin_edges # [B-1, ] , [B, ]

