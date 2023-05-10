#!/usr/bin/env python3
'''main function
'''
from typing import List
from asyncio import as_completed, create_task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''should return the list of all the delays (float values).
    '''
    arr = []
    for i in range(n):
        num = (task_wait_random(max_delay))
        arr.append(num)
    sorted = []
    for j in as_completed(arr):
        sorted.append(await j)

    return(sorted)
