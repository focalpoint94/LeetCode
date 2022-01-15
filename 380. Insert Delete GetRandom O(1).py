class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        idx = self.dict[val]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.dict[self.arr[idx]] = idx
        self.dict.pop(self.arr[-1])
        self.arr.pop()
        return True
        
    def getRandom(self) -> int:
        import random
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
