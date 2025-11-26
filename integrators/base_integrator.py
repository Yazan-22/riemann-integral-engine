from abc import ABC, abstractmethod

class BaseIntegrator(ABC):
    def __init__(self, func, a, b):            
        if not callable(func):
            raise TypeError("func must be callable")

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("a and b must be numbers")

        if a >= b:
            raise ValueError("a must be less than b")
        
        self.func = func
        self.a = a
        self.b = b

    @abstractmethod
    def compute(self, n):
        """compute the integral approximation with n subintervals."""
        pass