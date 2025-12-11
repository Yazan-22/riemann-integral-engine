from parser.function_parser import parse_function
from engine.integration_engine import IntegrationEngine
from engine.exceptions import IntegrationError
from integrators.left_riemann_integrator import LeftRiemannIntegrator
from integrators.right_riemann_integrator import RightRiemannIntegrator
from integrators.midpoint_integrator import MidpointIntegrator
from plotting import plot_function_and_area

def choose_method():
    print("Select integration method:")
    print("1. Left Riemann sum")
    print("2. Right Riemann sum")
    print("3. Midpoint Riemann sum")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        return "left"
    elif choice == "2":
        return "right"
    elif choice == "3":
        return "midpoint"
    else:
        raise IntegrationError("Invalid integration method choice.")

def main():
    try:
        print("Enter the function f(x) (example: sin(x), x**2 + 3*x, exp(x))")
        func_str = input("f(x) = ").lower()

        a = float(input("Enter lower bound a: "))
        b = float(input("Enter upper bound b: "))

        func, parsed_a, parsed_b = parse_function(func_str,a,b)

        n = int(input("Enter number of intervals n: "))

        method_choice = choose_method()

        engine = IntegrationEngine(func, a, b)
        result = engine.run(method_choice,n)

        print(f"Approximate integral value: {result}")
        plot_choice = input("Do you want to plot the function and area? [Y/N]: ").strip().lower()

        if plot_choice == "Y":
            try:
                plot_function_and_area(func, a, b, n, method_choice)
            except Exception as exc:
                print("Could not generate plot:", exc)

    except IntegrationError as e:
        print("Integration error:", e)
    except Exception as e:
        print("Unexpected error:", e)          

if __name__ == "__main__":
    main()        
