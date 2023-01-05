#!/usr/bin/env python3
"""module for creating multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function returns a function that takes an argument"""
    def multiplier_f(num: float, mutiplier: float=multiplier) -> float:
        """function mutilplies num by multiplier"""
        return num * multiplier
    return multiplier_f
