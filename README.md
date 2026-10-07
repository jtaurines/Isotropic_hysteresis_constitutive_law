# Isotropic magnetic hysteresis constitutive law

Python implementation of an analytical isotropic magnetic hysteresis constitutive law with two hysteresis parameters.

This project provides an analytical model for describing magnetic hysteresis based on the Langevin function and its inverse. It is intended for the simulation of magnetization curves under varying magnetic fields.

## Installation

### 1. Clone the repository

Clone the GitHub repository and move into the project directory:

```bash
git clone https://github.com/jtaurines/Isotropic_hysteresis_constitutive_law.git
cd Isotropic_hysteresis_constitutive_law
```

### 2. Create a Python virtual environment

It is recommended to use a virtual environment to isolate the project's dependencies.

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the project

With the virtual environment activated:

```bash
python -m pip install -e .
```

This installs the `isomag` package and its required dependencies.

## Run the example

An example is provided in the `examples/` directory.

Run it with:

```bash
python examples/example.py
```

The example computes and plots a magnetic hysteresis loop using the analytical constitutive law.

## Use the package in your own Python code

Once the package is installed, the main functions can be imported directly:

```python
from isomag.hysteresis import hysteresis_analytique
```

The hysteresis model can then be used in your own Python scripts or numerical simulations.

## Project structure

```text
Isotropic_hysteresis_constitutive_law/
├── LICENSE
├── README.md
├── .gitignore
├── pyproject.toml
├── examples/
│   └── example.py
└── src/
    └── isomag/
        ├── __init__.py
        ├── constants.py
        ├── hysteresis.py
        ├── inv_man.py
        └── man.py
```

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

The required Python dependencies are automatically installed with:

```bash
python -m pip install -e .
```

## License

This project is distributed under the Apache License 2.0.

See the [`LICENSE`](LICENSE) file for the full license text.

