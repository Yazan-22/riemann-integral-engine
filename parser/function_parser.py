import math
from typing import Callable
from .exceptions import InvalidFunctionExpressionError
from .exceptions import  InvalidLimitError

def parse_function(expression: str, a, b) -> tuple[Callable[[float], float], float, float]:

    allowed_names = {
        
    "abs": abs,
    "round": round,
    "pow": pow,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "exp": math.exp,
    
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "sqrt": math.sqrt,
    "floor": math.floor,
    "ceil": math.ceil,
    "fabs": math.fabs,
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    }

    try:
        test_env = allowed_names.copy()
        test_env["x"] = 1.0
        eval(expression, {"__builtins__": {}}, test_env)
    except Exception:
        raise InvalidFunctionExpressionError("Invalid Function Expression Error")   

    try:
        a =float(a)
        b =float(b)
    except ValueError:
        raise InvalidLimitError("Integration limits must be numeric.")
    
    if a >= b:
        raise InvalidLimitError("Lower limit must be less than upper limit.")
    
    def f(x: float) -> float:
        env = allowed_names.copy()
        env["x"] = x
        return eval(expression, {"__builtins__": {}}, env)

    return f, a, b