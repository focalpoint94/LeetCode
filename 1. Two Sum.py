class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numDict[val] = idx
        numDict = {}
        for i, num in enumerate(nums):
            if target - num in numDict:
                return [i, numDict[target-num]]
            numDict[num] = i
        return [0, 0]
