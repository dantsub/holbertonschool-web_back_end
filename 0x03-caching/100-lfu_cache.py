#!/usr/bin/python3
"""LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class

    Args:
        BaseCaching (class): Basic class for this class
    """
    def __init__(self):
        super().__init__()
        self.__keys = []
        self.__counter = {}

    def put(self, key, item):
        """put item into cache_data with LFU algorithm

        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            self.discard()
        if key and item:
            if key not in self.cache_data:
                self.__counter[key] = 1
                self.__keys.append(key)
            else:
                self.__counter[key] += 1
            self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary

        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        self.__counter[key] += 1
        return self.cache_data[key]

    def discard(self):
        """discard item and print
        """
        low = 0
        for i in range(3):
            key1 = self.__keys[low]
            key2 = self.__keys[i + 1]
            if self.__counter[key1] > self.__counter[key2]:
                low = i + 1
        discard = self.__keys.pop(low)
        del self.__counter[discard]
        del self.cache_data[discard]
        print('DISCARD: {}'.format(discard))
