#!/usr/bin/env python3
"""make multiplier module"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def f(n: float) -> float:
        return n * multiplier
    return f
