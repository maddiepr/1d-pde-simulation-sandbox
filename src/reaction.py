"""
reaction.py

This module defines functions related to the reaction term in 1D reaction-diffusion simulations using Monte Carlo methods.

Each function defines how particle weights should be updated at each step based on a spatially dependent reaction rate. These update rules are designed to be passed as callable functions to the core diffusion simulator.

Key Responsibilities:
- Define reaction rate functions R(x)
- Implement weight update logic based on R(x) and step size
- Provide modular interfaces for use in multiple simulation setups.

Typical Usage:
- Used in 'run_reaction.py' by passing a weight update function to the simulator
- Can be customized to reflect different reaction dynamics

Planned Extensions:
- Support for time-dependent or nonlinear reaction rates
- Integration with external data or parametertized fields
"""