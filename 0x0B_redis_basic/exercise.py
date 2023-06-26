#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """ Wrapper method """
        self._redis.incr(key)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store history of inputs and outputs into list """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args) -> Any:
        """ Wrapper method """
        input_data = args
        output_data = method(self, *args)
        self._redis.rpush(key + ":inputs", str(input_data))
        self._redis.rpush(key + ":outputs", str(output_data))
        return output_data

    return wrapper


def replay(method: Callable) -> None:
    """ Display the history of calls """
    zip("", "".lrange(""))


class Cache:
    """ Writing strings to Redis """

    def __init__(self):
        """ Create redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key, store it in Redis and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, int, float]:
        """ Get data and convert it the desired format """
        res = self._redis.get(key)
        if res is None:
            return None
        if fn is not None:
            return fn(res)
        return res

    def get_str(self, key: str) -> str:
        """Convert data to str """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Convert data to int """
        return self.get(key, fn=int)
