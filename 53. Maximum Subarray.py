class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = -int(1e9)
        reg = 0
        for num in nums:
            reg += num
            ret = max(ret, reg)
            if reg < 0:
                reg = 0
        return ret
