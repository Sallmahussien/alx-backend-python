#!/usr/bin/env python3
"""Defines function measure_time"""

import asyncio

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time for wait_n function"""
    start_time: float = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time: float = end_time - start_time

    return total_time / n
