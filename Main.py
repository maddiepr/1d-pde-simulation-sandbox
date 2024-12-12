import numpy as np
from Simulate_realizations import simulate_diffusion_source_realizations
from Parameters import parameters

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Main
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''Define Arguments'''
seed = parameters["seed"]
number_of_steps = parameters["number_of_steps"]
number_of_realizations = parameters["number_of_realizations"]
final_time = parameters["final_time"]
diffusion_coefficient = parameters["diffusion_coefficient"]
intial_positions = parameters["intial_positions"]
intial_T_values = parameters["intial_T_values"]


simulate_diffusion_source_realizations(number_of_steps, 
                             number_of_realizations, 
                             diffusion_coefficient, 
                             final_time / number_of_steps, 
                             intial_positions,
                             intial_T_values, 
                             seed )
