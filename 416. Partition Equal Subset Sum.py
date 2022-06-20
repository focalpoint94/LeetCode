from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        self.nums = nums
        target = sum(nums) // 2
        return self.backtrack(0, target)
    
    @lru_cache(maxsize=None)
    def backtrack(self, idx, target):
        if target < 0:
            return False
        if target == 0:
            return True
        if idx == len(self.nums):
            return False
        if self.backtrack(idx + 1, target - self.nums[idx]):
            return True
        if self.backtrack(idx + 1, target):
            return True
        return False
