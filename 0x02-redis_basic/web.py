import requests
import redis


def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL
    tracks the access count, and caches the result
    with expiration.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the specified URL.
    """
    # Initialize Redis client
    redis_client = redis.Redis()

    # Increment access count
    url_count_key = f"count:{url}"
    redis_client.incr(url_count_key)

    # Check if the page is cached
    cached_data = redis_client.get(url)
    if cached_data is not None:
        return cached_data.decode("utf-8")

    # If not cached, fetch the page using requests
    response = requests.get(url)
    html_content = response.text

    # Cache the result with an expiration time of 10 seconds
    redis_client.setex(url, 10, html_content)

    return html_content
