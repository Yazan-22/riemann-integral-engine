from .base_integrator import BaseIntegrator

class MidpointIntegrator(BaseIntegrator):
    def compute(self, n):
        if n <= 0:
            raise ValueError("n must be a positive integer")
        h = (self.b - self.a) / n
        total = 0

        for i in range(n):
            x_mid = self.a + (i + 0.5) * h
            total += self.func(x_mid)

        return total * h
