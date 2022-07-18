from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None, None)
        def backtrack(i, summed):
            if i == len(nums):
                if summed == target:
                    return 1
                return 0
            return backtrack(i+1, summed+nums[i]) + backtrack(i+1, summed-nums[i])
        return backtrack(0, 0)
