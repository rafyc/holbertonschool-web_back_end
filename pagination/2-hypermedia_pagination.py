#!/usr/bin/env python3
"""
Main file
"""
import csv
from math import ceil
from typing import List, Dict, Any, Tuple, Optional

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return the data in the range
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        corect_index: Tuple[int, int] = index_range(page, page_size)
        start_index: int = corect_index[0]
        end_index: int = corect_index[1]
        data: List[List] = self.dataset()

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        '''
        '''

        data: List[List] = self.get_page(page, page_size)
        dataset_size: int = len(self.dataset())
        total_pages: int = ceil(dataset_size / page_size)
        page_size: int = len(data)
        next_page: Optional[int] = page + 1 if page < total_pages else None
        prev_page: Optional[int] = page - 1 if page > 1 else None

        dict: Dict[str, Any] = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return dict
