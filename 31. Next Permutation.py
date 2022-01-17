class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            return nums.sort()
        
        swap_idx, swap_val = None, int(1e9)
        for j in range(i, len(nums)):
            if nums[j] > nums[i-1] and nums[j] < swap_val:
                swap_val = nums[j]
                swap_idx = j
        
        nums[i-1], nums[swap_idx] = nums[swap_idx], nums[i-1]
        nums[i:] = sorted(nums[i:])
