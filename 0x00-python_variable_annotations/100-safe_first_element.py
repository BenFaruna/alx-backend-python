#!/usr/bin/env python3
"""module for duck typing elements in a list"""
from typing import Any, Sequence, Union, NewType, Type

NoneType = NewType('NoneType', Type[None])


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """function returns the first element of lst"""
    if lst:
        return lst[0]
    else:
        return None
