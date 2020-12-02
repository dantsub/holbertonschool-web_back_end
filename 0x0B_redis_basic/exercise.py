#!/usr/bin/env python3
""" Redis exercises module
"""
import redis
from typing import Union, Callable, List, Optional
import uuid
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count amount of calls to method """
    key = method.__qualname__

    @wraps(method)
    def counter_wrapper(self, *args, **kwargs):
        """ Wrapper for method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return counter_wrapper


def call_history(method: Callable) -> Callable:
    """ Store history of inputs and outputs for a function """
    input_list_key = method.__qualname__ + ":inputs"
    output_list_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def set_history(self, *args, **kwargs):
        """ Set list keys to wrapped function """
        self._redis.rpush(input_list_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, str(res))
        return res

    return set_history


def replay(method: Callable) -> None:
    """ Ouput log of actions taken on method """
    counter_key = method.__qualname__
    input_list_key = method.__qualname__ + ':inputs'
    output_list_key = method.__qualname__ + ':outputs'
    this = method.__self__

    counter = this.get_str(counter_key)
    history = list(zip(this.get_list(input_list_key),
                       this.get_list(output_list_key)))
    print("{} was called {} times:".format(counter_key, counter))
    for call in history:
        value = this.get_str(call[0])
        key = this.get_str(call[1])
        print("{}(*{}) -> {}".format(counter_key, value, key))


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Instantiate Redis """
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store any type of data in Redis """
        key = str(uuid.uuid4())
        self._redis[key] = data
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """ Get value in db, convert data back to desired format """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, b: bytes) -> str:
        """ Convert bytes to str """
        return b.decode('utf-8')

    def get_int(self, b: bytes) -> int:
        """ Convert bytes to int """
        return int.from_bytes(b, sys.byteorder)

    def get_list(self, k: str) -> List:
        """ Convert bytes from store to list """
        return self._redis.lrange(k, 0, -1)
