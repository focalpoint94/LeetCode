class Solution:
    def canJump(self, nums):
        destination = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= destination:
                destination = i
        return destination == 0
