#!/usr/bin/env python3
"""module for creating multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_f(num: float, mutiplier: float=multiplier) -> float:
        return num * multiplier
    return multiplier_f
