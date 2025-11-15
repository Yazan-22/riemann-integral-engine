# riemann-integral-engine

Project Description
Riemann Integral Engine is a Python application that approximates definite integrals using numerical Riemann sum techniques.
The system accepts a user-defined mathematical function and integration limits, validates them, and computes approximations using multiple Riemann sum variants (left, right, and midpoint).
The project is designed with modular structure, type hints, and clear documentation to support future extensions such as plotting and accuracy analysis.

Author: Yazan Almohammad (working individually)

Repository Link: https://github.com/Yazan-22/riemann-integral-engine

Features:
--Iteration 0 Features (Design Phase)
1-Set up project module structure (parser module, integrators module, engine module).
2-Implement basic function parser to accept:
  * a function as string (e.g. "x**2 + 3*x")
  * integration limits a and b.
3-Define base classes and protocols for Riemann sum integrators (left, right, midpoint), without full implementation.
4-Add initial error-handling structure for invalid function expressions and invalid limits.

--Iteration 1 Features (First Implementation)
1-Implement Left Riemann Sum integrator.
2-Implement Right Riemann Sum integrator.
3-Implement Midpoint Riemann Sum integrator.
4-Implement the Integration Engine class that selects and runs a chosen Riemann method.
5-Add improved validation and error handling (invalid expressions, zero-step intervals, non-numeric inputs).

--Iteration 2 Features (Expansion + Assistant Feature)
1-Add optional plotting of the function and shaded area using matplotlib.
2-Add Trapezoidal method or Simpson method (depending on assistant’s request).
3-Add tests for all modules (pytest) and ensure good coverage.
4-Add performance profiling and create a short report on bottlenecks and suggested optimizations.
