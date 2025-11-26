from typing import Callable
from ..integrators.left_riemann_integrator import LeftRiemmannIntegrator
from ..integrators.right_riemann_integrator import RightRiemmanIntegrator
from ..integrators.midpoint_integrator import MidpointIntegrator
from .exceptions import (
    UnknownMethodError,
    InvalidStepError,
    InvalidEngineInputError,
)

class IntegrationEngine:
    """
    Selects and runs a Riemann sum integration method.
    """

    def __init__(self, func: Callable[[float], float], a: float, b: float):
        if not callable(func):
            raise InvalidEngineInputError("Function must be callable.")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise InvalidEngineInputError("Limits a and b must be numeric.")
        if a >= b:
            raise InvalidEngineInputError("Lower limit must be less than upper limit.")

        self.func = func
        self.a = a
        self.b = b

    def run(self, method: str, n: int) -> float:
        """
        Run a chosen integration method.
        method: 'left', 'right', 'midpoint'
        n: number of subintervals
        """
        if not isinstance(n, int) or n <= 0:
            raise InvalidStepError("n must be a positive integer")

        method = method.lower()

        if method == "left":
            integrator = LeftRiemmannIntegrator(self.func, self.a, self.b)
        elif method == "right":
            integrator = RightRiemmanIntegrator(self.func, self.a, self.b)
        elif method == "midpoint":
            integrator = MidpointIntegrator(self.func, self.a, self.b)
        else:
            raise UnknownMethodError("Unknown method. Choose: 'left', 'right', 'midpoint'.")

        return integrator.compute(n)
