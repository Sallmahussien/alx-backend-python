#!/usr/bin/env python3
"""Defines safe_first_element function"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of the iterable or None"""
    if lst:
        return lst[0]
    else:
        return None
