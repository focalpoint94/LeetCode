class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cnt = 1
                while num + 1 in nums:
                    num += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest
