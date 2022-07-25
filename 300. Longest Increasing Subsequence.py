from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        array = []
        for num in nums:
            idx = bisect_left(array, num)
            if idx == len(array):
                array.append(num)
            else:
                array[idx] = num
        return len(array)
