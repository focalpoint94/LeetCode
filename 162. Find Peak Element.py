class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        INT_MAX = int(1e12)
        nums = [-INT_MAX] + nums + [-INT_MAX]
        def isPeak(idx):
            if nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]:
                return True
            return False
        
        left, right = 1, len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if isPeak(mid):
                return mid - 1
            if nums[mid-1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
