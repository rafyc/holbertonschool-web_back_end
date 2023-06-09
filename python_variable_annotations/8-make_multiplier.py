#!/usr/bin/env python3
'''
main function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function that return a callback'''
    def callback(number: float) -> float:
        '''the callback function'''
        return (number * multiplier)
    return callback
