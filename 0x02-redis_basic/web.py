#!/usr/bin/env python3
""" Web cache module requests"""


import requests
import redis
from typing import Callable
from functools import wraps

redis= redis.Redis()


def count_request(fun: Callable):
    """
	count_request the call to requests
	"""

    @wraps(fun)
    def wrapper(url):
        """
		 This is a function that will count_request
		 """
        redis.incr(f"count:{url}")
        expiration_count = redis.get(f"cached:{url}")
        if expiration_count:
            return expiration_count.decode('utf-8')
        result = fun(url)
        redis.setex(f"cached:{url}", 10, html)
        return result

    return wrapper


@count_request
def get_page(url: str) -> str:
     """get page self descriptive
    """
    response = requests.get(url)
    return response.text
