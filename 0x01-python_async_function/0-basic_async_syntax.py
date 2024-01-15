#!/usr/bin/env python3
"""Defines function wait_random"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """Waits for a random delay and returns it"""
    random_delay = random.uniform(0, max_delay)

    await asyncio.sleep(random_delay)

    return random_delay
