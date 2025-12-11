from __future__ import annotations

from typing import Callable, Iterable, Literal, Optional

import numpy as np
import matplotlib.pyplot as plt


MethodName = Literal["left", "right", "midpoint", "trapezoidal"]


def _sample_points_for_method(
    a: float, b: float, n: int, method: MethodName
) -> np.ndarray:
    h = (b - a) / n

    if method == "left":
        return np.array([a + i * h for i in range(n)])
    if method == "right":
        return np.array([a + i * h for i in range(1, n + 1)])
    if method == "midpoint":
        return np.array([a + (i + 0.5) * h for i in range(n)])
    if method == "trapezoidal":
        # for visualization, we use the endpoints (a, ..., b)
        return np.array([a + i * h for i in range(n + 1)])

    raise ValueError(f"Unsupported method for plotting: {method!r}")


def plot_function_and_area(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int,
    method: MethodName,
    title: Optional[str] = None,
    show: bool = True,
    save_path: Optional[str] = None,
) -> None:
    """
    Plot f(x) on [a, b], shade the approximate area, and mark sample points.

    This does not call the integration engine; it assumes you already
    computed the approximate value separately.
    """
    xs_dense = np.linspace(a, b, 400)
    ys_dense = np.array([func(x) for x in xs_dense])

    x_samples = _sample_points_for_method(a, b, n, method)
    y_samples = np.array([func(x) for x in x_samples])

    fig, ax = plt.subplots()

    # Curve
    ax.plot(xs_dense, ys_dense, label="f(x)")

    # Shaded area under the curve (for visual intuition)
    ax.fill_between(xs_dense, ys_dense, alpha=0.3, label="Approximate area")

    # Sample points (where the integrator "looks")
    ax.scatter(x_samples, y_samples, marker="o", label=f"{method.capitalize()} sample points")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    if title is None:
        title = f"Riemann / {method.capitalize()} approximation, n={n}"
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    if save_path is not None:
        fig.savefig(save_path, bbox_inches="tight")

    if show:
        plt.show()

    plt.close(fig)
