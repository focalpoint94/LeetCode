class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]
        return num
