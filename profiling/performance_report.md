# Performance Report – Riemann Integral Engine

## Setup

- Function: f(x) = x²
- Interval: [0, 1]
- Methods: left, right, midpoint, trapezoidal
- Subintervals: n ∈ {100, 1 000, 10 000}
- Profiled using cProfile and pstats.

## Observations

1. **Overall cost is linear in n**:
   The dominant cost is repeated evaluation of f(x) inside loops of length n.

2. **Midpoint and trapezoidal methods**:
   They perform a similar number of function evaluations as left/right methods,
   so their running times are of the same order.

3. **No obvious algorithmic bottlenecks**:
   All integrators use simple Python loops and float arithmetic.

## Suggested Optimizations

1. **Vectorization (optional)**:
   For large n, consider using NumPy arrays to evaluate f(x) on all sample
   points at once. This can significantly speed up the computation.

2. **Reduce Python overhead**:
   - Avoid recomputing constants (step size h) inside loops.
   - Cache the function in a local variable inside loops to avoid attribute
     lookups.

3. **Parallelism for very large n**:
   If n becomes extremely large, the interval [a, b] can be split and
   processed in parallel using multiprocessing or numba (if allowed by the
   project constraints).

At the current scale (n up to around 10 000), the engine already performs
well for typical educational and demonstration purposes.
