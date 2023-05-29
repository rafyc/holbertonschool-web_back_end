#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):

    if page == 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = page_size * page

    return(start_index, end_index)
