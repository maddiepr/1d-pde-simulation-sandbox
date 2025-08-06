"""
reaction.py

This module defines functions related to the reaction term in
1D reaction-diffusion simulations using Monte Carlo methods.

Each function defines how particle weights should be updated 
at each step based on a spatially dependent reaction rate. 
These update rules are designed to be passed as callable functions
to the core diffusion simulator.

Key Responsibilities:
- Define reaction rate functions R(x)
- Implement weight update logic based on R(x) and step size
- Provide modular interfaces for use in multiple simulation setups.

Typical Usage:
- Used in 'run_reaction.py' by passing a weight update function to 
the simulator
- Can be customized to reflect different reaction dynamics

Planned Extensions:
- Support for time-dependent or nonlinear reaction rates
- Integration with external data or parametertized fields
"""

import numpy as np

def get_reaction_function(reaction_type="linear", **kwargs):
    """
    Factory to return a reaction rate function R(x) based on specific type.

    Args:
        reaction_type (str): One of 'linear', 'quadratic', or 'gaussian'
        kwargs: Parameters for the selected function (e.g. alpha, center, width)

    Returns:
        Callable[[np.ndarray], np.ndarray]: Function that maps positions x to R(x)
    """
    if reaction_type == "linear":
        alpha = kwargs.get("alpha", 1.0)
        return lambda x: alpha * x
    
    elif reaction_type == "quadratic":
        alpha = kwargs.get("alpha", 1.0)
        return lambda x: alpha * x**2
    
    elif reaction_type == "gaussian":
        alpha = kwargs.get("alpha", 1.0)
        center = kwargs.get("center", 0.0)
        width = kwargs.get("width", 1.0)
        return lambda x: alpha * np.exp(-((x - center)**2) / (2 * width**2))
    
    else:
        raise ValueError(f"Unsupported reaction type: {reaction_type}")