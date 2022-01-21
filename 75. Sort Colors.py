class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        count[2] = count[1] + count[0]
        count[1] = count[0]
        
        for i in range(count[1]):
            nums[i] = 0
        for i in range(count[1], count[2]):
            nums[i] = 1
        for i in range(count[2], len(nums)):
            nums[i] = 2
