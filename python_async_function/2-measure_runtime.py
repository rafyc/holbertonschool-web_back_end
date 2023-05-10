#!/usr/bin/env python3
'''main function
'''
import time
from typing import List
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure time
    '''
    sart_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    read_time = end_time - sart_time
    return (read_time / n)
