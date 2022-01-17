class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        i = 0
        for num in nums:
            if num != prev:
                nums[i] = num
                prev = num
                i += 1
        return i
