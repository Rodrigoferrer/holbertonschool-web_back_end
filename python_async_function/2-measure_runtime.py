#!/usr/bin/env python3
"""
Measure the runtime of wait_n
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per operation.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        float: Average execution time per operation (total_time / n)
    """
    start_time = time.time()
    
    # Run the wait_n coroutine
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Calculate and return the average time
    return total_time / n
