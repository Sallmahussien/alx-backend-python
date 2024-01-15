#!/usr/bin/env python3
"""Defines function task_wait_n"""

import asyncio

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    delays_list: List[float] = []

    for idx in range(n):
        delay: asyncio.Task = task_wait_random(max_delay)
        delay_result: float = await delay

        delays_list.append(delay_result)

    return sorted(delays_list)
