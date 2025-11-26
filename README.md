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
---------------------------------------------------------------------------------------------------------
Parser Module (parser/)
The parser module is responsible for validating user input and converting the function expression and integration limits into a safe, executable form for the integration engine. It ensures that only allowed mathematical operations are used and that integration bounds are valid before passing data to the Riemann integrators.

Folder Contents:
1_ function_parser.py:
  Contains the main parsing logic for user-defined function expressions and integration limits.
  Responsibilities:
  a_ Accept a mathematical function provided as a string (e.g., "x**2 + sin(x)").
  b_ Validate the expression using a restricted evaluation environment (only safe math functions).
  c_ Raise a custom error if the expression is invalid.
  d_ Validate integration limits a and b.
  e_ Ensure limits are numeric and satisfy a < b.
  f_ Return:
        * A callable Python function f(x)
        * The validated lower limit a
        * The validated upper limit b

2_ exceptions.py:
  Defines custom exception classes used by the parser module.
  Contains:
  a_ InvalidFunctionExpressionError — raised when a function expression contains invalid syntax or disallowed operations.
  b_ InvalidLimitError — raised when integration limits are missing, non-numeric, or incorrectly ordered.

3_ init.py:
   Marks the parser folder as a Python package.

---------------------------------------------------------------------------------------------------------

Integrators Module (integrators/)
The integrators module contains the core numerical algorithms used to approximate definite integrals using Riemann sums. Each integrator implements the same interface (the compute() method) but uses a different Riemann strategy: left endpoints, right endpoints, or midpoints.
This module is built using object-oriented design, following the Strategy Pattern.
All integrators inherit from a shared abstract base class. 

Folder Contents:
1_ base_integrator.py:
  Purpose:Defines the abstract base class BaseIntegrator, which ensures that all integrators follow the same structure.
  Responsibilities:
  a_ Stores the function f(x) being integrated.
  b_ Stores the interval limits a and b.
  c_ Validates:
      * func must be callable.
      * Limits must be numeric
      * a < b must hold.
  d_ Declares the abstract method compute(n) that child classes must implement.    

2_ left_integrator.py:
    Purpose:Implements the Left Riemann Sum method.
    Formula: the summation from i = 0 to n-1 for f(a+ih)h 
    Key behaviors:
      a_ Uses left endpoints of each subinterval.
      b_ Ensures n is a positive integer.
      c_ Computes:
        * step size: h = (b - a) / n
        * sample points: x_i = a + i * h
        * sum of function values.

3_ right_integrator.py:
    Purpose:Implements the Right Riemann Sum method.
    Formula: the summation from i = 1 to n for f(a+ih)h   
    Key behaviors:
      a_ Uses right endpoints of each subinterval.
      b_ Validates n.
      c_ Computes:
          * step size: h = (b - a) / n
          * sample points: x_i = a + i * h
          * weighted sum of values

4_ midpoint_integrator.py:
    Purpose:Implements the Midpoint Riemann Sum method.  
    Formula: the summation from i = 0 to n-1 for f(a+(i+1/2)h)h        
    Key behaviors:
    a_ Uses midpoint of each subinterval for improved accuracy.
    b_ Validates n
    c_ Computes:
        * step size: h = (b - a) / n
        * midpoint sample: x_mid = a + (i + 0.5) * h