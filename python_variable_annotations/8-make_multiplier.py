#!/usr/bin/env python3
'''
main function
'''
from collections.abc import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function that return a callback
    '''
    def callback(number: int) -> float:
        '''the callback function
        '''
        return (number * multiplier)
    return callback
