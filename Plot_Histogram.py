import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import describe
from Parameters import parameters
import scipy.integrate as integrate
from Plot_Exact_Sol import plot_exact_solution_diffusion_source


def plot_normalized_histogram(counts, bin_edges, num_realizations, positions):

      # Find width of bins and divide normalized histogram by that
      bin_width = bin_edges[1] - bin_edges[0] # float
    
      # Find normalized Histogram
      normalized_density = counts/(bin_width*num_realizations)

      # Find the location of the center bins
      bin_centers = np.squeeze(0.5 * (bin_edges[:-1] + bin_edges[1:])) # [B, 1] -> [B, ]

      # Add titles and axis labels
      num_of_steps = parameters["number_of_steps"]
      final_time = parameters["final_time"]
    
      # Find Statistics
      mean_code = normalized_density.mean()
      std_dev_code = normalized_density.std()
      var_code = normalized_density.var()
      max_code = normalized_density.max()

      # Plot normalized histogram
      plt.title(f"Normalized Histogram\nRealizations: {num_of_steps}, "
            f"Time: {final_time} ")
      plt.xlabel("Position")
      plt.ylabel("Probability Density")

      # Find bounds for histogram
      max_pos = np.max(positions) # float
      min_pos = np.min(positions) # float
      
      # Plot Exact Solution
      x = np.linspace(min_pos, max_pos, 1000)
      exact_sol = plot_exact_solution_diffusion_source(1, final_time, 1, x)
      plt.plot(x, exact_sol)

      sol_mean = exact_sol.mean()
      sol_variance = exact_sol.var()
      sol_std = exact_sol.std()

      # Plot Normalized histogram
      plt.bar(bin_centers, normalized_density, width=bin_width, edgecolor='k')

      # Save Normalized Histogram
      plt.savefig('Post_Simulation_Data/position_distribution_not_normalized.png')

      print(mean_code, var_code, sol_mean, sol_variance)
      # Show Histogram
      plt.show()



      return None
