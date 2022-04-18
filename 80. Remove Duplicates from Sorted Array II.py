class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reg, freq = None, None
        k = 0
        for i, num in enumerate(nums):
            if reg != num:
                reg, freq = num, 1
            else:
                freq += 1
            if freq <= 2:
                nums[k] = num
                k += 1
        return k
