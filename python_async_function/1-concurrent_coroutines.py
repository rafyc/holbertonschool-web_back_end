#!/usr/bin/env python3
'''
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    arr = []
    for i in range(n):
        num = await wait_random(max_delay)
        arr.append(num)
    return(arr)
