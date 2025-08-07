"""
exact_solutions.py

This module provides analytical (exact solutions) for 1D PDEs used in the
Monte Carlo simulation framework, including reaction-diffusion and 
advection-diffusion case.

Each function assumes an initial delta function and returns the exact
solutions at a given point x and time t, parameterized by diffusion and
reaction or advection coefficients.

Typical Usage:
    from src.exact_solutions import reaction_solution, advection_solution
    y = reaction_solution(x_vals, t=0.1, alpha=1.0, kappa=1.0)
"""

import numpy as np

def reaction_solution(x, t, alpha=1.0, kappa=1.0):
    """
    Exact solution to the 1D linear reaction-diffusion equation with delta IC.

    Args:
        x (float or np.ndarray): Spatial location(s)
        t (float): Time
        alpha (float): Reaction rate
        kappa (float): Diffusion coefficient

    Returns:
        np.ndarray: Values of T(x, t)
    """
    exponent = (kappa * alpha**2 * t**3) / 12 + (kappa * alpha * x * t)/2 - (kappa * x**2)/(4 * t)
    prefactor = 1 / np.sqrt(4 * np.pi * t)
    return prefactor * np.exp(exponent)

def advection_solution(x, t, alpha=1.0, kappa=1.0):
    """
    Exact soltion to the 1D advection-diffusion equation with spatially varying drift.

    Args:
        x (float or np.ndarray): Spatial location(s)
        t (float): Time
        alpha (float): Advection rate
        kappa (float): Diffusion coefficient

    Returns:
        np.ndarray: Values of T(x, t)
    """

    denominator = 2 * kappa * (np.exp(2 * alpha * t) - 1)
    prefactor = np.sqrt(alpha / (2 * np.pi * kappa * (np.exp(2 * alpha * t) - 1)))
    exponent = - (x**2 * alpha) / denominator + alpha * t
    return prefactor * np.exp(exponent)