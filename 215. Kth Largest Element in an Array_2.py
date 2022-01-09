import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k)
        
    def quick_select(self, nums, k):
        rand_idx = random.randint(0, len(nums)-1) if len(nums) >= 2 else 0
        pivot = nums[rand_idx]
        
        left = [num for num in nums if num > pivot]
        middle = [num for num in nums if num == pivot]
        right = [num for num in nums if num < pivot]
        
        L, M = len(left), len(middle)
        if k <= L:
            return self.quick_select(left, k)
        if k <= L + M:
            return middle[0]
        return self.quick_select(right, k-L-M)
