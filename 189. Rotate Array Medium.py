class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k %= len(nums)
        
        def inplace_reverse(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        
        inplace_reverse(0, len(nums)-1-k)
        inplace_reverse(len(nums)-k, len(nums)-1)
        inplace_reverse(0, len(nums)-1)        
