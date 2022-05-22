class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        def isPeak(i):
            if i == 0:
                return nums[0] > nums[1]
            if i == len(nums) - 1:
                return nums[-1] > nums[-2]
            return nums[i] > nums[i-1] and nums[i] > nums[i+1]
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if isPeak(mid):
                return mid
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
