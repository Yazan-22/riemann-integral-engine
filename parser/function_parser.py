import math
from typing import Callable
# from .exceptions rimport InvalidFunctionExpressionErro

def parse_function(expression: str, a, b) -> tuple[Callable[[float], float], float, float]:

    allowed_names = {
    "x": 0,
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
        eval(expression, {"__builtins__": {}}, allowed_names)
    except:
        print("InvalidFunctionExpressionError")    

    a = input("Enter the lower limit :")     
    b = input("Enter the upper limit :")
    try:
        a =float(a)
        b =float(b)
    except ValueError:
        print("Integration limits must be numeric.")
    
    if a >= b:
        print("Lower limit must be less than upper limit.")

f, a, b = parse_function("sin", -1, 1)
print(f)