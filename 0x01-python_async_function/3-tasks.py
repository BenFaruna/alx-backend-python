#!/usr/bin/env python3
"""module creates a Task class from function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function creates Task from coroutine"""
    result = wait_random(max_delay)
    return asyncio.Task(result)
