from __future__ import annotations
import cProfile
import pstats
from pathlib import Path

from engine.integration_engine import IntegrationEngine


def target_function():
    # Example: integrate x^2 from 0 to 1 with various n and methods
    func = lambda x: x**2  # noqa: E731
    a, b = 0.0, 1.0

    ns = [100, 1_000, 10_000]

    methods = ["left", "right", "midpoint", "trapezoidal"]

    for method in methods:
        for n in ns:
            engine = IntegrationEngine(func, a, b)
            _ = engine.run(method, n)


def main():
    profile_output = Path("profiling") / "integration_profile.prof"
    profile_output.parent.mkdir(exist_ok=True)

    profiler = cProfile.Profile()
    profiler.enable()

    target_function()

    profiler.disable()
    profiler.dump_stats(str(profile_output))

    stats = pstats.Stats(profiler).strip_dirs().sort_stats("cumtime")
    stats.print_stats(20)


if __name__ == "__main__":
    main()
