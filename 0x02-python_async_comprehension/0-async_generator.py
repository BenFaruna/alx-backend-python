#!/usr/bin/env python3
'''module for async generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    '''function returns 10 random generated numbers'''
    for i in range(10):
        yield random.uniform(0, 10)