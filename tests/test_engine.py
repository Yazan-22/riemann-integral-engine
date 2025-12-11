import pytest

from riemann_integral_engine.engine.integration_engine import IntegrationEngine
from riemann_integral_engine.engine.exceptions import (
    InvalidEngineInputError,
    InvalidStepError,
    UnknownMethodError,
)


def test_engine_trapezoidal_constant():
    func = lambda x: 3.0  # noqa: E731
    a, b = 1.0, 4.0
    exact = 3.0 * (b - a)

    engine = IntegrationEngine(func, a, b, method="trapezoidal")
    result = engine.run(20)

    assert result == pytest.approx(exact)


def test_engine_left_linear():
    func = lambda x: x  # noqa: E731
    a, b = 0.0, 1.0
    exact = 0.5

    engine = IntegrationEngine(func, a, b, method="left")
    result = engine.run(1_000)
    assert result == pytest.approx(exact, rel=1e-3)


def test_invalid_method_raises():
    func = lambda x: x  # noqa: E731
    with pytest.raises(UnknownMethodError):
        IntegrationEngine(func, 0, 1, method="weird")


def test_invalid_limits_raises():
    func = lambda x: x  # noqa: E731
    with pytest.raises(InvalidEngineInputError):
        IntegrationEngine(func, 1, 0, method="left")


def test_invalid_n_raises():
    func = lambda x: x  # noqa: E731
    engine = IntegrationEngine(func, 0, 1, method="left")

    with pytest.raises(InvalidStepError):
        engine.run(0)
