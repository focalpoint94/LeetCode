class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k %= len(nums)
        self.inplace_reverse(nums, 0, len(nums)-1-k)
        self.inplace_reverse(nums, len(nums)-k, len(nums)-1)
        self.inplace_reverse(nums, 0, len(nums)-1)        
        
    def inplace_reverse(self, arr, l, r):
        if not arr:
            return
        while l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
