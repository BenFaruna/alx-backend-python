#!/usr/bin/env python3
"""module for concurrent coroutines"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function calls the wait_random function n times with max_delay"""
    waiting = []
    result = []
    for i in range(n):
        waiting.append(task_wait_random(max_delay))

    for i in asyncio.as_completed(waiting):
        result.append(await i)

    return result
