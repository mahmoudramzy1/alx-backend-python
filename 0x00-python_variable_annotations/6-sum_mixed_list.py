#!/usr/bin/env python3
"""module to sum a list of mixed floats and ints"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function to sum a list of mixed floats and ints"""
    return sum(mxd_lst)
