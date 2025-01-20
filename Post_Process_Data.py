import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from Diy_Histogram import hist_diy
from Save_values import save_values
from scipy.stats import describe
from Plot_Exact_Sol import plot_exact_solution_diffusion_source
from Parameters import parameters
from Plot_Histogram import plot_normalized_histogram


'''Define Arguments'''
seed = parameters["seed"]
num_of_steps = parameters["number_of_steps"]
num_realizations = parameters["number_of_realizations"]
final_time = parameters["final_time"]
diffusion_coefficient = parameters["diffusion_coefficient"]
intial_positions = parameters["intial_positions"]
intial_T_values = parameters["intial_T_values"]
number_of_bins = parameters["number_of_bins_in_histogram"]

# Grab positions data
position_file_path = '/Users/maddiepreston/Desktop/scripts/Diffusion_Source_code/Post_simulation_data/Final_Positions.txt'
positions = pd.read_csv(position_file_path, header=None ).to_numpy()

# Grab T value data
T_vals_file_path = '/Users/maddiepreston/Desktop/scripts/Diffusion_Source_code/Post_simulation_data/Final_T_values.txt'
T_vals = pd.read_csv(T_vals_file_path, header=None ).to_numpy()

# Find the number of counts in each bin 
counts, bin_edges = hist_diy(number_of_bins, positions, num_realizations, T_vals)

plot_normalized_histogram(counts, bin_edges, num_realizations, positions)


'''
x = np.linspace(positions.min(), positions.max(), 100)
# Plot as a bar chart for normalized histogram
#plt.bar(bin_edges[:0], normalized_density, width=bin_width, alpha=0.7, color='blue', label='Normalized Histogram')
#plt.plot(x, counts)

print(counts.sum())

#plt.plot(x, counts)
plt.savefig('Post_Simulation_Data/position_distribution_not_normalized.png')

sol = plot_exact_solution_diffusion_source(1,
                                         0.01, 
                                         1,
                                         x)

plt.plot(x, sol)
plt.plot(x, normalized_density)
plt.savefig('Post_Simulation_Data/position_distribution_normalized.png')
'''

'''
#plt.plot(x, sol)
plt.plot(x, counts)
#plt.plot(x, normalized_density)

plt.show()
plt.savefig('Post_Simulation_Data/position_distribution_normalized.png')

# Get summary statistics and save to .txt file
#stats_summary = describe(counts).to_numpy()
#save_values(stats_summary, "Statistics")
'''
'''
# Visualization
plt.plot(T_vals)
#plt.hist(positions[0], bins=20)
plt.title("Position Distribution")
plt.xlabel("Position")
plt.ylabel("Frequency")
plt.savefig('Post_Simulation_Data/position_distribution.png')
plt.show()
'''
