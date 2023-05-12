#!/usr/bin/python3
'''LIFOCache module
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    put method & get method
    '''
    def put(self, key, item):
        '''put an item in cache and delet the first if fullp
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            li = list(self.cache_data.keys())[-2]
            self.cache_data.pop(li)
            print(f"DISCARD: {li}")

    def get(self, key):
        '''Get an item in the cache"
        '''
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        return None
