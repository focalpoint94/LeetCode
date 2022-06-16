class Solution:
    def findMin(self, nums: List[int]) -> int:
        ret = float('inf')
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            ret = min(ret, num)
            if num < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return ret
