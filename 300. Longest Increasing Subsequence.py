class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        from bisect import bisect_left
        ret = 1
        for i in range(1, len(nums)):
            idx = bisect_left(temp, nums[i])
            if idx == len(temp):
                temp.append(nums[i])
            else:
                temp[idx] = nums[i]
            ret = max(ret, len(temp))
        return ret
