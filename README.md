# Monte Carlo Simulation of 1D Advection-Diffusion Equations

This repository contains Python code for simulating 1D advection-diffusion equations with divergence-dependent velocity fields using Monte Carlo methods. It serves as an exploratory sandbox for

- Testing numerical strategies
- Analyzing stochastic behavior of particle systems
- Comparing simulation output to analytical solutions
- Laying the groundwork for higher-dimensional implementations

##  🔍 Project Overview

The simulation solves PDEs of the form:

∂T/∂t = ∂/∂x (D(x) ∂T/∂x) − ∂/∂x (u(x) T)

where:
- D(x) is a spatially dependent diffusion coefficient
- u(x) is a divergence-dependent drift field

Particles undergo stochastic motion with path weights governed by the PDE. The final density is estimated via weighted histograms and compared with known exact solutions where possible.

---

## 🗂 Project Structure

```text
monte-carlo-1d/
├── run_reaction.py         # Script to run reaction-diffusion simulation
├── run_advection.py        # Script to run the advection-diffusion simulation

├── src/
│  ├── __init__.py
│  ├── diffusion.py         # Shared core diffusion logic
│  ├── reaction.py          # Reaction term logic 
│  ├── advection.py         # Advection term logic 
│  └── utils.py             # Histogram, plotting, and post-processing utilities

├── data/                   # Output particle data and weights

├── notebooks/              # Notebooks for visualization and exploration
│  ├── visualize_reaction.ipynb
│  └── visualize_advection.ipynb

├── docs/                   # Documentation, example plots, and reference figures
│  ├── sample_plot.png

├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠 Getting Started

#### 1. Clone the Repository

```bash 
git clone https://github.com/maddiepr/monte-carlo-1d.git
cd monte-carlo-1d
```

#### 2. Install Dependencies

```bash
python -m venv env
source env/bin/activate # or env\Scripts\activate on Windows
pip install -r requirements.txt
```

#### 3. Run a Simulation

```bash
python run_reaction.py
python run_advection.py
```

You can adjust parameters in Parameters.py

---

## 🚧 Project Status

This is an early-stage, research-driven codebase. While core logic is functional and documented, structure and performance optimizations are ongoing. Furture versions may modularize the code further and add 2D support (see related repo:monte-carlo-2d-mapping).

## 📎 License / Use

⚠️ This repository is provided for demonstration and reference only. Please do not reuse or distribute code without written permission.

## Author 

Madeline "Maddie" Preston
www.linkedin.com/in/madeline-preston | https://github.com/maddiepr

