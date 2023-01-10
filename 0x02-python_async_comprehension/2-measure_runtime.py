#!/usr/bin/env python3
"""module for measuring runtime"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime for async comprehension"""
    s = time.perf_counter()
    coroutines = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coroutines)
    e = time.perf_counter() - s
    return e
