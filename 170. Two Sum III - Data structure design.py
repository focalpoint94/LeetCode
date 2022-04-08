from collections import Counter
class TwoSum:

    def __init__(self):
        self.nums = Counter()

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for num in self.nums:
            target = value - num
            if target != num and target in self.nums:
                return True
            elif target == num and self.nums[target] >= 2:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
