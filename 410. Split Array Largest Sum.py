class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def num_bins(val):
            cnt = 0
            summed, maxsum = 0, 0
            for num in nums:
                summed += num
                if summed > val:
                    summed = num
                    cnt += 1
                maxsum = max(maxsum, summed)
            maxsum = max(maxsum, summed)
            return cnt + 1, maxsum
        
        ret = sum(nums)
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            k, maxsum = num_bins(mid)
            if k <= m:
                ret = min(ret, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ret
