import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import describe
from Parameters import parameters
import scipy.integrate as integrate


def plot_normalized_histogram(counts, bin_edges):
    
    #normalized_density = (counts - counts.mean())/(counts.std())
    
    area = np.trapz(counts)
    # Divide raw counts by the sum of counts
    #normalized_density = counts * scalar # [B, ]
    #normalized_density = preprocessing.normalize(counts)

    # Find width of bins and divide normalized histogram by that
    bin_width = bin_edges[1] - bin_edges[0] # float
    #normalized_density = normalized_hist / bin_width # [B, ]

    normalized_density = counts/area

    


    # Find the location of the center bins
    bin_centers = np.squeeze(0.5 * (bin_edges[:-1] + bin_edges[1:])) # [B, 1] -> [B, ]

    # Add titles and axis labels
    num_of_steps = parameters["number_of_steps"]
    final_time = parameters["final_time"]
    
    # Find Statistics
    mean = normalized_density.mean()
    std_dev = normalized_density.std()
    var = normalized_density.var()
    max = normalized_density.max()

    # Plot normalized histogram
    plt.title(f"Normalized Histogram\nRealizations: {num_of_steps}, "
          f"Time: {final_time}, "
          f"Mean: {mean}"
          f"Variance: {var}"
          f"Max: {max}"
          f"Std_Dev: {std_dev}")
    plt.xlabel("Position")
    plt.ylabel("Probability Density")

    # Plot Normalized histogram
    plt.bar(bin_centers, normalized_density, width=bin_width, edgecolor='k')

    # Save Normalized Histogram
    plt.savefig('Post_Simulation_Data/position_distribution_not_normalized.png')

    # Show Histogram
    plt.show()

    return None
