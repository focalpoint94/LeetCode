class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cnt = 0
                while num in nums:
                    num += 1
                    cnt += 1
                ret = max(ret, cnt)
        return ret
