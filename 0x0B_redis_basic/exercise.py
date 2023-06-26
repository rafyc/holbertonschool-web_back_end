#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

@wraps(method)
def wrapper(self, *args):
    self._redis.incr(key)
    return method(self, *args)
return wrapper

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        res = self._redis.get(key)
        if res is None:
            return None
        if fn is not None:
            return fn(res)
        return res

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
