#!/usr/bin/env python3
"""Defines make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return multipy function"""
    def multiply(n: float) -> float:
        """Multiply multiplier with n"""
        return n * multiplier

    return multiply
