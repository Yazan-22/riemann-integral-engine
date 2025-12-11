import math
import pytest

from riemann_integral_engine.parser.function_parser import parse_function
from riemann_integral_engine.parser.exceptions import (
    InvalidFunctionExpressionError,
    InvalidLimitError,
)


def test_parse_function_valid():
    expr = "x**2 + 2*x"
    func, a, b = parse_function(expr, 0, 1)

    assert a == 0.0
    assert b == 1.0
    assert pytest.approx(func(0.0)) == 0.0
    assert pytest.approx(func(1.0)) == 3.0


def test_parse_function_uses_math():
    expr = "sin(x) + cos(x)"
    func, a, b = parse_function(expr, -math.pi, math.pi)

    assert a == pytest.approx(-math.pi)
    assert b == pytest.approx(math.pi)
    assert pytest.approx(func(0.0)) == 1.0  # sin(0) + cos(0)


def test_invalid_expression_raises():
    with pytest.raises(InvalidFunctionExpressionError):
        parse_function("import os; os.system('rm -rf /')", 0, 1)  # illegal


def test_invalid_limits_raises():
    # Non-numeric
    with pytest.raises(InvalidLimitError):
        parse_function("x", "a", 1)

    # a >= b
    with pytest.raises(InvalidLimitError):
        parse_function("x", 1, 0)
