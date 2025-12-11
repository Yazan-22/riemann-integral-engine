import pytest

from integrators.left_riemann_integrator import LeftRiemannIntegrator
from integrators.right_riemann_integrator import RightRiemannIntegrator
from integrators.midpoint_integrator import MidpointIntegrator
from integrators.trapezoidal_integrator import TrapezoidalIntegrator

def test_constant_function_exact():
    func = lambda x: 2.0  # noqa: E731
    a, b = 0.0, 5.0
    exact = 2.0 * (b - a)

    for Integrator in [
        LeftRiemannIntegrator,
        RightRiemannIntegrator,
        MidpointIntegrator,
        TrapezoidalIntegrator,
    ]:
        integrator = Integrator(func, a, b)
        result = integrator.compute(10)
        assert result == pytest.approx(exact)


def test_linear_function_converges():
    func = lambda x: x  # noqa: E731
    a, b = 0.0, 1.0
    exact = 0.5  # ∫_0^1 x dx

    n = 1_000

    left = LeftRiemannIntegrator(func, a, b).compute(n)
    right = RightRiemannIntegrator(func, a, b).compute(n)
    mid = MidpointIntegrator(func, a, b).compute(n)
    trap = TrapezoidalIntegrator(func, a, b).compute(n)

    assert left == pytest.approx(exact, rel=1e-3)
    assert right == pytest.approx(exact, rel=1e-3)
    assert mid == pytest.approx(exact, rel=1e-4)
    assert trap == pytest.approx(exact, rel=1e-4)


def test_invalid_n_raises():
    func = lambda x: x  # noqa: E731
    a, b = 0.0, 1.0

    integrator = TrapezoidalIntegrator(func, a, b)
    with pytest.raises(ValueError):
        integrator.compute(0)
