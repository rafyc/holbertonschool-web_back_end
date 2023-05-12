#!/usr/bin/python3
'''BasicCache module
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    put method & get method
    '''
    def put(self, key, item):
        '''Add an item in the cache"
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
        pass

    def get(self, key):
        '''Get an item in the cache"
        '''
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        return None
