#!/usr/bin/env python3
'''main function
'''
from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    '''
    return asyncio task
    '''
    task = create_task(wait_random(max_delay))
    return task
