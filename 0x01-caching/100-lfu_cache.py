#!/usr/bin/python3
"""LFUCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits
    from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """method that puts a new item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.count[key] += 1
                self.queue.remove(key)
                self.queue.append(key)
                return
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.count[key] = 1
                self.queue.append(key)
            else:
                freq = min(self.count.values())
                least = [k for k in self.count if self.count[k] == freq]
                if len(least) == 1:
                    discard = least[0]
                else:
                    for i in self.queue:
                        if i in least:
                            discard = i
                            break
                self.queue.remove(discard)
                self.cache_data.pop(discard)
                self.count.pop(discard)
                print("DISCARD: {}".format(discard))
                self.cache_data[key] = item
                self.count[key] = 1
                self.queue.append(key)

    def get(self, key):
        """method that retrieves the item from the cache"""
        if key and key in self.cache_data:
            self.count[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
