from .base_integrator import BaseIntegrator

class LeftRiemmannIntegrator(BaseIntegrator):
    def compute(self,n):
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        h = (self.b - self.a) / n
        total = 0  

        for i in range(n):
            x_i = self.a + i * h   
            total += self.func(x_i)

        return total * h             