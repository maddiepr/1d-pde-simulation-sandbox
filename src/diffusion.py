"""
diffusion.py

This module contains the core logic for simulating 1D diffusion processes using Monte Carlo methods.

The main function simulates discrete particle stepping under stochastic motion, with optional support for reaction or advection terms passed as callable update rules.

Key Responsibilities:
- Initialize particle positions
- Perform Brownian stepping (with optional drift)
- Update particle weights step-by-step
- Return or save final positions and weights for statistical analysis

Typical Usage:
- Called by entry-point scripts (e.g. 'run_reaction.py', 'run_advection.py')
- Can be configured via direct parameters or external config modules

Planned Extensions:
- Support for spatially dependent diffusion coefficients D(x)
- Optional boundary handing (reflecting, absorbing)
- Vectorized stepping for performance optimization
"""