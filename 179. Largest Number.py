class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x: str(x)*100, reverse=True)
        ret = ''.join([str(num) for num in nums]).lstrip('0')
        return ret if ret else "0"
