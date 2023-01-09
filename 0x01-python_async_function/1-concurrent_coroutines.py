#!/usr/bin/env python3
"""module for concurrent coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function calls the wait_random function n times with max_delay"""
    waiting = []
    result = []
    for i in range(n):
        waiting.append(wait_random(max_delay))

    for i in asyncio.as_completed(waiting):
        result.append(await i)

    return result
