
# Contributing to Civil Engineering Toolbox

Thank you for your interest in contributing!

Civil Engineering Toolbox is an open-source initiative
dedicated to developing accessible computational
tools for civil engineers, researchers and students.

Contributions from the international engineering
community are welcome.

## 1. Ways to Contribute

You can help by:

- Developing new engineering algorithms.
- Reporting bugs and numerical inaccuracies.
- Improving existing functions.
- Writing technical documentation.
- Adding reproducible engineering examples.
- Expanding automated test coverage.
- Reviewing engineering assumptions and calculations.

## 2. Engineering Disciplines

Contributions may cover:

- Geotechnical Engineering.
- Structural Engineering.
- Transportation Engineering.
- Hydraulics and Hydrology.
- Geospatial Engineering.
- Engineering Data Analytics.
- Computational and Numerical Methods.

New disciplines may be introduced when justified
by the scope and maturity of the project.

## 3. Before Contributing

Please check existing Issues and Pull Requests.

For substantial features, open a GitHub Issue
describing the proposed functionality before
starting development.

Your proposal should explain:

1. Engineering problem being addressed.
2. Intended users and applications.
3. Mathematical or physical formulation.
4. Required inputs and expected outputs.
5. Relevant engineering references.
6. Proposed validation methodology.

## 4. Development Workflow

1. Fork the repository.
2. Create a descriptive feature branch.
3. Implement your changes.
4. Add or update unit tests.
5. Document assumptions and limitations.
6. Run the test suite locally.
7. Submit a Pull Request.

Example branch names:

- feat/structural-beam-analysis
- feat/geotechnical-settlement
- fix/consolidation-validation
- docs/hydraulic-methods

## 5. Code Quality

Python contributions should follow PEP 8
where practical.

Functions should include:

- Descriptive names.
- Type annotations where appropriate.
- Clear docstrings.
- Defined input and output units.
- Meaningful exceptions.
- Reproducible examples.

Avoid unnecessary dependencies.

## 6. Engineering Validation

Every new engineering algorithm should include:

- Mathematical or physical assumptions.
- Governing equations.
- References to established sources.
- Valid input domains.
- Numerical limitations.
- Automated tests.
- Independent reference comparisons
  whenever practical.

A successful test run does not automatically
establish engineering validity.

## 7. Testing

Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the test suite:

```bash
python -m pytest -v
```

All existing tests should pass before submitting
a Pull Request.

## 8. Documentation

Scientific modules should include documentation
covering:

- Engineering background.
- Mathematical formulation.
- Model assumptions.
- Units and parameter definitions.
- Usage examples.
- Numerical verification.
- Known limitations.
- Engineering references.

## 9. Licensing and Intellectual Property

Contributions must be compatible with the
GNU General Public License v3.0.

Contributors must have the right to submit
their code and supporting materials.

Do not submit proprietary source code,
confidential engineering information,
restricted datasets or third-party materials
without appropriate authorization.

## 10. Community Standards

Please communicate respectfully and constructively.

Technical disagreements should focus on evidence,
engineering reasoning and reproducible results.

Harassment, discrimination and personal attacks
are not acceptable.

## 11. Pull Request Checklist

- [ ] My contribution addresses a defined problem.
- [ ] I have documented engineering assumptions.
- [ ] I have added or updated tests.
- [ ] All tests pass locally.
- [ ] I have updated relevant documentation.
- [ ] I have reviewed license compatibility.
- [ ] I have not included confidential information.

Thank you for helping make engineering knowledge
more accessible.

---

Civil Engineering Toolbox

Engineering knowledge should be shared.

Ad Victoriam!
