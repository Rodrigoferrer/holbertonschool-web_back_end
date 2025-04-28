#!/usr/bin/env python3
"""
Create an asyncio.Task for wait_random
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random

    Returns:
        asyncio.Task: Task for wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
