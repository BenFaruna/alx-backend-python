#!/usr/bin/env python3
"""module for type annotations"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """function return value of key"""
    if key in dct:
        return dct[key]
    else:
        return default
