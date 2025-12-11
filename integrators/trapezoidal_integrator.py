from __future__ import annotations

from .base_integrator import BaseIntegrator


class TrapezoidalIntegrator(BaseIntegrator):
    """
    Implements the trapezoidal rule for numerical integration.

    Approximation:
        ∫_a^b f(x) dx ≈ h * [ (f(a) + f(b)) / 2 + Σ_{i=1}^{n-1} f(a + i h) ]
    where h = (b - a) / n
    """

    def compute(self, n: int) -> float:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer.")

        h = (self.b - self.a) / n
        total = 0.5 * (self.func(self.a) + self.func(self.b))

        for i in range(1, n):
            x_i = self.a + i * h
            total += self.func(x_i)

        return total * h
