from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sums = [0] * N
        sums[0] = nums[0]
        for i in range(1, N):
            sums[i] = sums[i-1] + nums[i]
        
        ret = 0
        c = Counter()
        for i in range(N):
            if sums[i] == k:
                ret += 1
            ret += c[sums[i]-k]
            c[sums[i]] += 1
        return ret
