#!/usr/bin/env python3
'''
main function
'''
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    '''
    return [(i, len(i)) for i in lst]
