class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i, num in enumerate(nums):
            num = abs(num)
            if nums[num-1] < 0:
                ret.append(num)
            else:
                nums[num-1] *= -1
        return ret
