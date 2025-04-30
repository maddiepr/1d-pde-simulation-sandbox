# 1D Divergence-Dependent Simulation (Starter Repo)

This repository contains exploratory code for simulating 1D advection-diffusion equations with divergence-dependent velocity fields using Monte Carlo methods. It serves as a sandbox for testing numerical strategies, analyzing stochastic behavior, and refining ideas for higher-dimensional extensions.

## 🔍 Project Overview

The simulation models particle paths governed by PDEs of the form:

∂T/∂t = ∇·(D(x)∇T) - ∇·(u(x)T)

Key focuses include:
- Implementation of divergence-dependent drift
- Histogram-based density estimation
- Comparison with exact solutions
- Post-simulation statistics and visualization

## 🧠 Main Components

| Function Name             | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `Main`                   | Entry point for running simulations                                     |
| `Parameters`             | Defines simulation parameters (drift, diffusion, domain, time, etc.)    |
| `Simulate_Realizations`  | Runs the core Monte Carlo solver across realizations                    |
| `Diy_Histogram`          | Computes weighted 1D histograms for solution density                    |
| `Plot_Histogram`         | Visualizes Monte Carlo density output                                   |
| `Plot_Exact_Solution`    | Plots theoretical solution for comparison                               |
| `Plot_Best_Fit`          | Fits and visualizes approximation vs. exact                            |
| `Save_values`            | Saves simulation output and bin data                                    |
| `Post_Process_Data`      | Computes statistics and normalizations post-simulation                  |


## 🚧 Status

This is a **starter-level, exploratory research repo**, intended for internal prototyping and method testing. Code is documented where relevant, but structure and performance are still in development.

## 📎 License / Use

⚠️ This repository is provided for demonstration and reference only. Please do not reuse or distribute code without written permission.

