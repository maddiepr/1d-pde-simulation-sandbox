"""
exact_solutions.py

Exact solution functions for 1D PDEs.

Currently implemented for:
- Linear reaction term: reaction_solution()
- Linear advection velocity: advection_solution()

NOTE:
These formulas apply only to the linear cases.
They will NOT be correct for:
    - Quadratic reaction types
    - Gaussian reaction types
    - Nonlinear advection velocity profiles

In those cases, no closed-form exact solution is provided, and 
comparison to an exact solution should be skipped.
"""

import numpy as np

def reaction_solution(x, t, alpha=1.0, kappa=1.0, x0=0.0):
    """
    Exact solution to the 1D linear reaction-diffusion equation with delta IC.

    Args:
        x (float or np.ndarray): Spatial location(s)
        t (float): Time
        alpha (float): Reaction rate
        kappa (float): Diffusion coefficient
        x0 (float): Initial Condition

    Returns:
        np.ndarray: Values of T(x, t)
    """
    denom = 2 * kappa * (np.exp(2 * alpha * t) - 1)
    coeff = np.sqrt(alpha / (np.pi * denom))
    exponent = -alpha * ((x - x0)**2) / denom + alpha * t
    return coeff * np.exp(exponent)

def advection_solution(x, t, alpha=1.0, kappa=1.0, x0=0.0):
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
    exponent = - ((x-x0)**2 * alpha) / denominator + alpha * t
    return prefactor * np.exp(exponent)