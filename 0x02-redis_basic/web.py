#!/usr/bin/env python3
"""
    Module: Redis Cache Counting with Expiration
"""

from functools import wraps
import redis
import requests
from typing import Callable

redis_cache = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
        Decortator for cache counting with expiration
    """
    @wraps(method)
    def wrapper(url):
        """
            Wrapper for decorator
        """
        redis_cache.incr(f"count:{url}")
        html = redis_cache.get(f"cached:{url}")
        if html:
            return html.decode('utf-8')
        html_ = method(url)
        redis_cache.setex(f"cached:{url}", 10, html_)
        return html_

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
        The function uses the requests module to obtain the HTML content of a
        particular URL and returns it
    """
    results = requests.get(url)
    return results.text
