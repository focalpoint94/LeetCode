class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x: str(x)*10, reverse=True)
        ret = ''
        for num in nums:
            ret += str(num)
        return ret.lstrip('0') if ret.lstrip('0') else '0'
