#!/usr/bin/env python3
'''module for async generator'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''function returns 10 random generated numbers'''
    for i in range(10):
        yield random.uniform(0, 10)
