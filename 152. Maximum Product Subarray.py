class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = -float('inf')
        prod = 1
        for num in nums:
            ret = max(ret, num)
            if num == 0:
                prod = 1
                continue
            prod *= num
            ret = max(ret, prod)
        prod = 1
        for num in nums[::-1]:
            if num == 0:
                prod = 1
                continue
            prod *= num
            ret = max(ret, prod)
        return ret
