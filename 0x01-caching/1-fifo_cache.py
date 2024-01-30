#!/usr/bin/python3
"""FIFOCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits
    from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """method that puts a new item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.queue.append(key)
            else:
                discard = self.queue.pop(0)
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))
                self.cache_data[key] = item
                self.queue.append(key)

    def get(self, key):
        """method that retrieves the item from the cache"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
