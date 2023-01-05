#!/usr/bin/env python3
"""module for type annotations"""
from typing import Any, Mapping, NewType, TypeVar, Type, Union

NoneType = NewType('NoneType', Type[None])
T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, NoneType] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default