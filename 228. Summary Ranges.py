class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ret = []
        nums.append(nums[-1]+2)
        start = prev = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num == prev + 1:
                prev = num
            else:
                if start == prev:
                    ret.append(str(start))
                else:
                    ret.append(str(start)+"->"+str(prev))
                start = prev = nums[i]
        return ret
