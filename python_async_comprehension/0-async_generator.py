#!/usr/bin/env python3
'''
main function
'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
