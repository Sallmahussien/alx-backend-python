#!/usr/bin/env python3
"""Defines element_length function"""

from typing import Iterable, Sequence, List, Tuple

iterable = Iterable[Sequence]


def element_length(lst: iterable) -> List[Tuple[iterable, int]]:
    """Returns list of tuples with iterable and length of iterable"""
    return [(i, len(i)) for i in lst]
