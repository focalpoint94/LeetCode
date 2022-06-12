class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = float('inf')
        sum, i = 0, 0
        for j, num in enumerate(nums):
            sum += num
            while sum >= target:
                ret = min(ret, j - i + 1)
                sum -= nums[i]
                i += 1
        return ret if ret != float('inf') else 0
