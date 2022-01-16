class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        previ = None
        for i in range(len(nums)-3):
            if nums[i] == previ:
                continue
            prevj = None
            for j in range(i+1, len(nums)-2):
                if nums[j] == prevj:
                    continue
                preSum = nums[i] + nums[j]
                l, r = j + 1, len(nums) - 1
                while l < r:
                    summation = preSum + nums[l] + nums[r]
                    if summation < target:
                        l += 1
                    elif summation > target:
                        r -= 1
                    else:
                        ret.append([nums[i], nums[j], nums[l], nums[r]])
                        prevl, prevr = nums[l], nums[r]
                        while l <= r and nums[l] == prevl:
                            l += 1
                        while r >= l and nums[r] == prevr:
                            r -= 1
                prevj = nums[j]
            previ = nums[i]
        return ret
