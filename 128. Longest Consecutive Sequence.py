class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 0
        for num in nums:
            if num-1 in nums:
                continue
            t = num
            cnt = 0
            while t in nums:
                cnt += 1
                t = t + 1
            ret = max(ret, cnt)
        return ret
