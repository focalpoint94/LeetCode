class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, ret = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i + 1, N - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return ret
