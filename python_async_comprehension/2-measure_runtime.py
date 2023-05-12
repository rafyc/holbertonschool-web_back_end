#!/usr/bin/env python3
'''main function
'''

import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure runtime
    """
    sart_time = time.time()
    await asyncio.gather(async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = time.time()
    read_time = end_time - sart_time
    return read_time
