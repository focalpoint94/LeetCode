class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums, 0, len(nums)-1, target)
        
    def binary_search(self, nums, left, right, target):
        if left > right:
            return [-1, -1]
        mid = (left + right) // 2
        mid_val = nums[mid]
        if mid_val > target:
            return self.binary_search(nums, left, mid-1, target)
        elif mid_val < target:
            return self.binary_search(nums, mid+1, right, target)
        else:
            i1, i2 = self.binary_search(nums, left, mid-1, target)
            i3, i4 = self.binary_search(nums, mid+1, right, target)
            if i1 == -1 and i4 == -1:
                return [mid, mid]
            if i1 == -1 and i4 != -1:
                return [mid, i4]
            if i1 != -1 and i4 == -1:
                return [i1, mid]
            return [i1, i4]
