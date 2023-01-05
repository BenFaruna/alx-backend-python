#!/usr/bin/env python3
"""module for converting to key value"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function return a tuple contain k and cube of v"""
    return k, v ** 2
