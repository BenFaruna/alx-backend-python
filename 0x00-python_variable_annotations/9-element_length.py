#!/usr/bin/env python3
"""module for getting iterable length"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function returns a list of tuples"""
    return [(i, len(i)) for i in lst]
