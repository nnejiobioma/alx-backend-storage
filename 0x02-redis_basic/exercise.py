#!/usr/bin/env python3
""" REDIS DATABASE PROJECT """

from functools import wraps
from uuid import uuid4
from typing import Optional,Union, Callable

import redis


def count_calls(method: Callable) -> Callable:
  """
		system to count how many
    	times methods of the Cache class are called.
	"""
    key = method.__qualname__

    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """
        Wrap
        :param self:
        :param args:
        :param kwargs:
        :return:
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
		
    return wrapped


def call_history(method: Callable) -> Callable:
   """
	 	This add its input parameters to one list
    	in redis, and store its output into another list.
	 """
    @wraps(method)
    def wrapped(**kwargs, self, *args, ):
    """
			function that count
		"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(**kwargs, self, *args, ))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapped


def replay(fn: Callable):
  """
    		The helps to Display
			history of calls
	"""
    r = redis.Redis()
    function_name = fn.__qualname__
    count = r.get(function_name)
    try:
        count = int(count.decode("utf-8"))
    except Exception:
        count = 0
    print(f"{function_name} was called {count} times:")
    inputs = r.lrange(f"{function_name}:inputs", 0, -1)
    outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    for one, two in zip(inputs, outputs):
        try:
            one = one.decode('utf-8')
        except Exception:
            one = ""
        try:
            two = two.decode('utf-8')
        except Exception:
            two = ""
        print(f"{function_name}(*{one}) -> {two}")


class Cache:
  """
			implement cache strategy with redis
	"""
    def __init__(self):
    """
		This helps to get a number
		"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
		This generate a random key (e.g. using uuid),
         store the input data in Redis using the
          random key and return the key.
		Helps to get a data that will be saved
		"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
			This helps to extract the information
			saved in redis
		"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ 
			Parameterizes a value from redis to str
			convert the data back
			to the desired format
		"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
			A parameters that value from redis to int
			get a number
		"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
