#!/usr/bin/env python3
"""return tuple of string and square of float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of string and square of float"""
    return (k, v * v)
