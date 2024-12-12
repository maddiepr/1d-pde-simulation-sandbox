import matplotlib.pyplot as plt
from scipy.stats import norm

'''
Plots the best-fit Gaussian curve based on positions, mean, and std dev
    Variables:
        R: Number of realizations
    Parameters:
        x: [R, ] float
            x-values 
        mu_fit: float
            Mean of realizations
        sigma_fit: float
            Standard deviation of realizations
    Returns:
        None
'''

def plot_best_fit(x, 
                  mu_fit, 
                  sigma_fit):

    # Fit Statistics of the data into a normal PDF
    pdf_fit = norm.pdf(x, mu_fit, sigma_fit) # [1000, ]

    # Plot best fit PDF
    plt.plot(x, pdf_fit, 'g--', label=f'Best Fit: μ={mu_fit:.2f}, σ={sigma_fit:.2f}')

    return None