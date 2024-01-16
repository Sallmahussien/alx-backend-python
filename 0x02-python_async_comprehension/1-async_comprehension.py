#!/usr/bin/env python3
"""Defines function async_comprehension"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Feturn the 10 random numbers from async_generator"""

    return [num async for num in async_generator()]
