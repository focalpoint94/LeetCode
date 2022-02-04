class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.cnt = 0
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if self.cnt == self.capacity:
                self.cache.pop(next(iter(self.cache)))
                self.cnt -= 1
            self.cache[key] = value
            self.cnt += 1
