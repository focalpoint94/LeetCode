class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = int(1e9)
        N = len(nums)
        for i in range(N-2):
            l, r = i + 1, N - 1
            while l < r:
                summed = nums[i] + nums[l] + nums[r]
                if summed == target:
                    return target
                if abs(summed - target) < abs(ret - target):
                    ret = summed
                if summed < target:
                    l += 1
                elif summed > target:
                    r -= 1
        return ret
