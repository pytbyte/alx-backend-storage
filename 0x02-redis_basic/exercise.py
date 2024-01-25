import redis
import uuid
from typing import Callable
import functools


class Cache:
    def __init__(self):
        """
        Initializes a new Cache instance with a Redis
        client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """
        Stores the input data in Redis
        with a randomly generated key.

        Args:
            data: Data to be stored in Redis.
            Can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key
            used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """
        Retrieves data from Redis using the
        rovided key and optionally applies
        a conversion function.

        Args:
            key (str): The key used to retrieve data
            from Redis.
            fn (Callable, optional): A callable function
            to convert the data. Defaults to None.

        Returns:
            The retrieved data, optionally converted
            using the provided function.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str):
        """
        Retrieves a string from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the string from Redis.

        Returns:
            str: The retrieved string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """
        Retrieves an integer from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the integer from Redis.

        Returns:
            int: The retrieved integer.
        """
        return self.get(key, fn=int)

    @functools.wraps
    def count_calls(method):
        """
        Decorator to count the number of times a method is called.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data) -> str:
        """
        Stores the input data in Redis with a
        randomly generated key and increments
        the call count.

        Args:
            data: Data to be stored in Redis. Can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def replay(method):
        """
        Function to display the history of calls of a particular function.

        Args:
            method (Callable): The method to retrieve the history for.

        Returns:
            None
        """
        def wrapper(self):
            key = method.__qualname__
            inputs_key = f"{key}:inputs"
            outputs_key = f"{key}:outputs"

            inputs = self._redis.lrange(inputs_key, 0, -1)
            outputs = self._redis.lrange(outputs_key, 0, -1)

            print(f"{key} was called {len(inputs)} times:")
            for inp, out in zip(inputs, outputs):
                print(f"{key}(*{inp.decode()}) -> {out.decode()}")
        return wrapper

    @replay
    def store(self, data) -> str:
        """
        Stores the input data in Redis with a
        randomly generated key and records the
        input/output history.

        Args:
            data: Data to be stored in Redis. Can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
