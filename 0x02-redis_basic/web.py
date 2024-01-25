import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    @wraps(method)
    def invoker(url: str) -> str:
        # Increment the count for the URL
        redis_store.incr(f'count:{url}')
        
        # Try to retrieve the cached result
        result = redis_store.get(f'result:{url}')
        
        if result:
            # If cached result exists, return it
            return result.decode('utf-8')
        
        # If not cached, fetch the data using the original function
        result = method(url)
        
        # Set the result in the cache with a TTL of 10 seconds
        redis_store.setex(f'result:{url}', 10, result)
        
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    # Fetch the HTML content of the URL using requests
    response = requests.get(url)
    
    if response.status_code == 200:
        # Return the content if the request was successful
        return response.text
    else:
        # Handle other status codes if needed
        return f"Error: {response.status_code}"

