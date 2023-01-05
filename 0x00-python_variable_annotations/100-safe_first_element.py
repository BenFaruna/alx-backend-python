#!/usr/bin/env python3
"""module for duck typing elements in a list"""
from typing import Any, NewType, Sequence, Type, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function returns the first element of lst"""
    if lst:
        return lst[0]
    else:
        return None
