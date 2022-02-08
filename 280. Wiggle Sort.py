class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        big = False
        for i in range(len(nums)-1):
            if big:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            big = not big
