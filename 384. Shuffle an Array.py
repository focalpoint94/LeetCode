class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        import copy
        import random
        self.temp = copy.deepcopy(self.nums)
        for i in range(len(self.temp)-1):
            j = random.randint(i, len(self.temp)-1)
            self.temp[i], self.temp[j] = self.temp[j], self.temp[i]
        return self.temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
