#!/usr/bin/env python3
"""Defines function wait_n"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    delays_list: List[float] = []

    for idx in range(n):
        delay: float = await wait_random(max_delay)

        delays_list.append(delay)

    return sorted(delays_list)
