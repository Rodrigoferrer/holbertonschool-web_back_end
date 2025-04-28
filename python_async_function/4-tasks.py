#!/usr/bin/env python3
"""
Use task_wait_random to execute multiple coroutines concurrently
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay for each task_wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    # Create tasks using task_wait_random instead of wait_random directly
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Run the tasks concurrently and collect results as they complete
    results = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        results.append(delay)
    
    # Returns naturally sorted list (as results are added in order of completion)
    return results