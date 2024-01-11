#!/usr/bin/env python3
"""Defines sum_mixed_list function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of list of float or int numbers"""
    return float(sum(mxd_lst))