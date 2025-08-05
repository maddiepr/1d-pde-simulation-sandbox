"""
advection.py

This module defines the advection (drift) term for 1D advection-diffusion simulations using Monte Carlo methods.

It provides functions to compute spatially dependent velocity fields u(x), which influence the direction and magnitude of particle movement. These drift terms are intended to be integrated into the diffusion stepping logic.

Key Responsibilities:
- Define velocity field functions u(x)
- Provide hooks for modifying particle motion based on local drift
- Allow plug-and-play drift logic for different advection profiles

Typical Usage:
- Used in 'run_advection.py' to inject drift into the diffusion process
- Velocity functions passed to stepping routines in 'src.diffusion'

Planned Extensions:
- Support for divergence-dependent u(x) derived from ∂D/∂x
- Analytical comparisons with mapped PDEs or benchmark solutions
"""