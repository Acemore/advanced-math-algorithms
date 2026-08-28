# Advanced Math Algorithms

A robust Python repository dedicated to the implementation and automation of fundamental higher mathematics algorithms. The project spans linear algebra, mathematical analysis, and discrete mathematics, adhering to modern backend engineering standards.

## Technology Stack

* **Python 3.12+**
* **uv** — Ultra-fast Python package and environment manager
* **pytest** — Testing framework for mathematical validation
* **ruff** — Fast Python linter and code formatter
* **mypy** — Static type checker for strict type safety
* **pre-commit** — Git hooks management

## Project Structure

* `src/algebra/` — Linear algebra, matrix analysis, and SLAU solvers
* `src/analysis/` — Mathematical analysis (integrals, series, approximations)
* `src/discrete/` — Discrete mathematics, graph theory, and combinatorics
* `tests/` — Comprehensive suite of modular autotests

## Local Setup & Development

1. Sync dependencies and initialize the virtual environment:

   ```bash
   uv sync
   ```

2. Install git hooks for automated code quality checks:

   ```bash
   uv run pre-commit install
   ```

3. Run the test suite:

   ```bash
   uv run pytest
   ```
