import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        low, high = 0, len(nums) - 1
        while low < high:
            j = self.partition(nums, low, high)
            if j < k:
                low = j + 1
            elif j > k :
                high = j - 1
            else:
                return nums[k]
        return nums[low]
        
    def partition(self, nums, low, high):
        rand_idx = random.randint(low, high) if low != high else low
        # swap nums[high] and nums[rand_idx]
        nums[high], nums[rand_idx] = nums[rand_idx], nums[high]
        pivot = nums[high]
        
        left = low
        for i in range(low, high):
            if nums[i] <= pivot:
                # swap nums[i] and nums[left]
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        # swap nums[left] and nums[high]
        nums[left], nums[high] = nums[high], nums[left]
        return left
