class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" +str(upper)]
        ret = []
        start = lower
        nums.append(upper+1)
        for num in nums:
            end = num - 1
            if end >= start:
                if start == end:
                    ret.append(str(end))
                else:
                    ret.append(str(start) + "->" +str(end))
            start = num + 1
        return ret
