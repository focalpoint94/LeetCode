class Solution:
     def firstMissingPositive(self, nums):
        n = len(nums)
        elem = None
        for i in range(n):
            if 1 <= nums[i] <= n:
                elem = nums[i]
                break
        if not elem:
            return 1              
        
        # nums[i] is for i-1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = elem
        
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1
