class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = -float('inf')
        prod = 1
        for num in nums:
            prod *= num
            ret = max(ret, prod)
            if prod == 0:
                prod = 1
        prod = 1
        for num in nums[::-1]:
            prod *= num
            ret = max(ret, prod)
            if prod == 0:
                prod = 1
        return ret
