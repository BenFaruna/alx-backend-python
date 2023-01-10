#!/usr/bin/env python3
"""module for sync comprehension"""
import asyncio
from typing import AsyncGenerator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """return a list of random number using list comprehension"""
    result = [_ async for _ in async_generator()]
    return result
