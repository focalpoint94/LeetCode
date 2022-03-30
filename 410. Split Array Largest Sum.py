class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.nums = nums
        ret = sum(nums)
        left, right = max(nums), ret
        while left <= right:
            mid = (left + right) // 2
            numGroup = self.numGroup(mid)
            if numGroup <= m:
                ret = min(ret, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ret
        
    def numGroup(self, limit):
        ret = 0
        culm = 0
        for num in self.nums:
            culm += num
            if culm > limit:
                ret += 1
                culm = num
        return ret + 1
