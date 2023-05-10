#!/usr/bin/env python3
'''
'''

import asyncio, time, random

async def wait_random(max_delay = 10):
    num = random.uniform(0, max_delay)
    time.sleep(num)
    return num

