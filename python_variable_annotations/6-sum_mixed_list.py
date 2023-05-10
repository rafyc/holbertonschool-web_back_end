#!/usr/bin/env python3
'''
main function
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    takes a list mxd_lst of integers and floats and returns sum as a float
    '''
    return (sum(mxd_lst))
