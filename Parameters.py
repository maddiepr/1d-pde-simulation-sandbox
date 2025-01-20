import numpy as np

number_of_realizations = 10**6

parameters = {
    "seed": 52,
    "number_of_steps": 10**4 ,
    "number_of_realizations": number_of_realizations,
    "final_time": 1,
    "diffusion_coefficient": 1,
    "intial_positions": np.zeros(number_of_realizations),
    "intial_T_values": np.ones(number_of_realizations),
    "number_of_bins_in_histogram": 100,
}