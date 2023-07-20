#!/usr/bin/env python3
"""method that takes a data argument and returns a string"""
import redis
from typing import Union
import uuid


class Cache():
    """Cache class
    """
    def __init__(self):
        """store an instance of the Redis client
            as a private variable named _redi
        """
        self._redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string

        Args:
            data (Union[str, bytes, int , float]): _description_

        Returns:
            str: _description_
        """

        key = str(uuid.uuid4()) # lets convert uuid to string
        # Convert data to bytes if it's not already
        if not isinstance(data, bytes):
            # convert to byte if not an instance
            data = str(data).encode('utf-8')
            # Store the data in Redis with the generated key
        self._redis.set(key, data)
        return key
