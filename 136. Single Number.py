class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        from operator import xor
        return reduce(xor, nums)
#         num = nums[0]
#         for i in range(1, len(nums)):
#             num ^= nums[i]
#         return num
