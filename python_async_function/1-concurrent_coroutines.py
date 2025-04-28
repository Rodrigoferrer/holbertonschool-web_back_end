#!/usr/bin/env python3
"""
Concurrent coroutines module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    # Create a list of coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Run the coroutines concurrently and collect results as they complete
    results = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        results.append(delay)
    
    # Returns naturally sorted list (as results are added in order of completion)
    return results
