#!/usr/bin/env python3
"""module for measuring runtime of wait_n"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """functions measure runtime of the function wait_n"""
    # s = time.perf_counter()
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    # e = time.perf_counter() - s
    e = time.time() - s
    return e
