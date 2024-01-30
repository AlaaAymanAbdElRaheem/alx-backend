#!/usr/bin/python3
"""BasicCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits
    from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """method that puts a new item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """method that retrieves the item from the cache"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
