class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = -int(1e9)
        prod = 1
        for num in nums:
            prod *= num
            ret = max(ret, prod)
            if num == 0:
                prod = 1
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            ret = max(ret, prod)
            if nums[i] == 0:
                prod = 1
        return ret
