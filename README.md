
# 🏗️ Civil Engineering Data Analysis Toolbox

### Open-Source Computational Tools for Civil Engineers

**Engineering · Python · Data Science · Numerical Modelling**

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPLv3-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active_Development-orange?style=flat-square)

[![Python CI](https://github.com/TheWinterCoderDev/Data-Analysis-Toolbox-for-Civil-Engineers/actions/workflows/python-ci.yml/badge.svg?branch=refactor%2Fconsolidation-modernization)](https://github.com/TheWinterCoderDev/Data-Analysis-Toolbox-for-Civil-Engineers/actions/workflows/python-ci.yml)

---

## 🌍 About the Project

Civil Engineering Data Analysis Toolbox is an open-source
collection of Python-based computational tools designed
for civil engineers, researchers and engineering students.

The project aims to bridge traditional engineering
knowledge with modern programming, numerical methods,
scientific computing and data-driven technologies.

Its purpose is simple:

**To make practical computational engineering tools
accessible to engineers around the world.**

The repository is designed as a growing, multidisciplinary
library in which each engineering specialization can
contribute algorithms, scripts, examples and documentation.

---

## 🎯 Project Objectives

- Develop reusable Python tools for civil engineering.
- Provide accessible implementations of engineering models.
- Promote computational thinking in engineering education.
- Support data analysis, visualization and automation.
- Encourage reproducible engineering research.
- Share engineering knowledge through open-source software.
- Build a collaborative international engineering community.

---

## 🏗️ Engineering Disciplines

The long-term development roadmap includes the following
engineering domains.

| Discipline | Planned Applications | Status |
|---|---|---|
| Geotechnical Engineering | Consolidation, soil mechanics, foundations | Active |
| Structural Engineering | Structural analysis, matrix methods, FEM | Planned |
| Transportation Engineering | Railway systems, networks, mobility | Planned |
| Hydraulics & Hydrology | Flow analysis, hydraulic models | Planned |
| Geospatial Engineering | GIS, spatial analysis, terrain modelling | Planned |
| Data & Automation | Engineering analytics and workflow automation | Planned |

Each discipline will be developed incrementally through
independently documented modules.

---

## 🔬 Available Modules

### 01 — Geotechnical Engineering

#### Terzaghi 1D Consolidation

The first modernized module implements the classical
Fourier-series solution of Terzaghi's one-dimensional
consolidation equation.

It provides:

- Normalized excess porewater pressure calculations.
- Consolidation profiles for different time factors.
- Isochrone visualization using Matplotlib.
- Numerical input validation.
- Vectorized calculations using NumPy.
- Automated unit tests using pytest.

**Technology:** Python, NumPy, Matplotlib, pytest.

**Source code:**
[src/civil_engineering_toolbox/geotechnics/](src/civil_engineering_toolbox/geotechnics/)

**Example:**
[Terzaghi Isochrone Generator](examples/consolidation_1d_example.py)

**Original academic implementation:**
[Legacy Consolidation Script](consolidation_1_d/)

---

## 🚀 Getting Started

### Requirements

- Python 3.13
- NumPy
- Matplotlib

### Installation

Clone the repository:

```bash
git clone https://github.com/TheWinterCoderDev/Data-Analysis-Toolbox-for-Civil-Engineers.git

cd Data-Analysis-Toolbox-for-Civil-Engineers
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install the dependencies:

```bash
.venv/Scripts/python.exe -m pip install -r requirements-dev.txt
```

The commands above use the Windows virtual environment
layout. On Linux and macOS, use the Python interpreter
inside `.venv/bin/` instead.

### Running the Consolidation Example

On Windows:

```bash
.venv/Scripts/python.exe examples/consolidation_1d_example.py
```

The example generates normalized consolidation
isochrones and saves the resulting figure under:

```text
outputs/terzaghi_1d_isochrones.png
```

---

## 🧪 Testing & Quality Assurance

The repository uses pytest for automated numerical
verification.

Run the test suite:

```bash
.venv/Scripts/python.exe -m pytest -v
```

The current test suite includes eight tests covering:

- Drained boundary conditions.
- Pressure dissipation with time.
- Long-time analytical approximation.
- Vectorized spatial calculations.
- Invalid depth values.
- Negative time factors.
- Invalid Fourier-series parameters.
- Non-finite numerical inputs.

GitHub Actions runs these tests automatically on
configured branches and pull requests.

Passing tests demonstrate correctness for the tested
cases, not exhaustive numerical or engineering validation.

---

## 🗂️ Repository Organization

```text
Data-Analysis-Toolbox-for-Civil-Engineers/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── consolidation_1_d/
│   └── Original academic implementation
│
├── src/
│   └── civil_engineering_toolbox/
│       └── geotechnics/
│           └── consolidation_1d.py
│
├── examples/
│   └── consolidation_1d_example.py
│
├── tests/
│   ├── conftest.py
│   └── test_consolidation_1d.py
│
├── requirements-dev.txt
├── README.md
└── LICENSE
```

The directory structure will expand as new engineering
modules are developed.

---

## 🛣️ Development Roadmap

### Phase I — Geotechnical Foundations

- [x] Implement Terzaghi 1D consolidation.
- [x] Add reproducible isochrone generation.
- [x] Implement automated numerical tests.
- [x] Configure continuous integration.
- [ ] Expand numerical validation.
- [ ] Complete technical documentation.
- [ ] Publish the first modernized release.

### Phase II — Structural Engineering

- [ ] Introduce basic structural analysis algorithms.
- [ ] Develop matrix-based structural methods.
- [ ] Provide reproducible engineering examples.

### Phase III — Transportation Engineering

- [ ] Railway infrastructure analytics.
- [ ] Transportation network calculations.
- [ ] Mobility and infrastructure data analysis.

### Phase IV — Engineering Data & GIS

- [ ] Engineering data processing utilities.
- [ ] Geospatial analysis tools.
- [ ] Data visualization and automation examples.

Future modules will be prioritized according to
engineering relevance, maintainability and available
validation resources.

---

## 🤝 Contributing

Contributions from engineers, students and researchers
around the world are welcome.

You can contribute by:

- Reporting bugs or numerical inaccuracies.
- Proposing new engineering utilities.
- Improving documentation.
- Adding reproducible examples.
- Improving testing and numerical validation.

Please open a GitHub Issue to discuss substantial
new features before submitting a Pull Request.

All contributions must respect the project's license
and must not include confidential or proprietary
engineering information.

---

## ⚠️ Engineering Disclaimer

This project is intended for educational and research
purposes.

The software is not certified for professional,
industrial or safety-critical engineering applications.

Engineering calculations and numerical results must
be independently verified before use in real projects.

Users remain responsible for complying with applicable
engineering standards, regulations and professional
requirements.

---

## 📜 License

This project is distributed under the GNU General
Public License v3.0.

See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Raúl Galdeano Pazos — The Winter Coder**

Civil Engineering | Computational Engineering |
Data & Automation | Transportation Systems

[LinkedIn](https://www.linkedin.com/in/raulgaldeanopazos/)

---

### Engineering knowledge should be shared.

*Building practical tools for engineers, one script at a time.*

**Ad Victoriam! ❄️**
