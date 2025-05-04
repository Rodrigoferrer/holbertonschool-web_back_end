#!/usr/bin/env python3
"""Python3 Module"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that yields 10 random numbers
    after waiting 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
