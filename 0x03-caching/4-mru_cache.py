#!/usr/bin/python3
"""MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """FIFOCache class

    Args:
        BaseCaching (class): Basic class for this class
    """

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        pass

    def get(self, key):
        """get value of cache_data dictionary

        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
