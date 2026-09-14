"""Tiny read-through cache. Stdlib only.

Reads go stale after writes: `set` updates the store but never
invalidates the cached copy, so `get` keeps serving the old value.
"""


class Cache:
    def __init__(self):
        self._store = {}
        self._cache = {}
        self.hits = 0
        self.misses = 0

    def set(self, key, value):
        self._store[key] = value

    def get(self, key):
        if key in self._cache:
            self.hits += 1
            return self._cache[key]
        self.misses += 1
        value = self._store[key]
        self._cache[key] = value
        return value
