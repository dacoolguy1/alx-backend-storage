#!/usr/bin/env python3
"""method that takes a data argument and returns a string"""
import redis
from typing import Union, Optional
import uuid


class Cache():
    """Cache class
    """
    def __init__(self):
        """store an instance of the Redis client
            as a private variable named _redi
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string

        Args:
            data (Union[str, bytes, int , float]): _description_

        Returns:
            str: _description_
        """

        key = str(uuid.uuid4())  # lets convert uuid to string
        # Convert data to bytes if it's not already
        if not isinstance(data, bytes):
            # convert to byte if not an instance
            data = str(data).encode('utf-8')
            # Store the data in Redis with the generated key
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None) \
            -> Union[str, bytes, int, float]:
        """
        Get a key

        Args:
            key (str): _description_
            fn (Optional[callable], optional): _description_.
            convert the data back
            to the desired format

        Returns:
            Union[str, bytes, int, float]: _description_
        """
        data = self._redis.get(key)  # get this particular key
        if data is not None:
            if fn is not None:
                fn(data)
        return key

    def get_str(self, key: str) -> Optional[str]:
        """_summary_

        Args:
            self (_type_): _description_
        """
        return self.get(key,
                        fn=lambda d: d.decode('utf-8')
                        if d is not None else None)

    def get_int(self, key: str) -> Optional[int]:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            Optional[int]: _description_
        """
        return self.get(key, fn=lambda d: int(d) if d is not None else None)
