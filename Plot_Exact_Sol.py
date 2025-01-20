import numpy as np
import matplotlib.pyplot as plt

'''
Computes and plots the exact diffusion-source solution
    Parameters:
        alpha: float 
            Drift coefficient 
        time_fin: int 
            End time
        diff_coe: float 
            Diffusion coefficient 
        x: [1000, ] 
            X values for solution 
    Returns:
        None
'''


def plot_exact_solution_diffusion_source(alpha,
                                         time_fin, 
                                         diff_coe,
                                         x):

    # Generate diff-source equation
    exponent1 = time_fin**3  /( 12 ) # float
    exponent2 = (diff_coe * alpha * x * time_fin ) / 2 # [1000, ]
    exponent3 = (diff_coe * x**2 ) / (4 * time_fin) # [1000, ]

    numerator = np.exp(exponent1 + exponent2 - exponent3) # [1000, ]
    
    # Define exact solution
    exact_sol = numerator/ np.sqrt(4 * np.pi * time_fin) # [1000, ]
    
    # Calculate Statistics
    mean_theory = np.mean(exact_sol) 
    variance_theory = np.sum(((x - mean_theory)**2) * exact_sol) / np.sum(exact_sol)
    sigma_theory = np.sqrt(variance_theory)

    return exact_sol