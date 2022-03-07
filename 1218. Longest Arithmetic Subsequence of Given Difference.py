class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ret = 1
        numDict = {}
        for i in range(len(arr)-1, -1, -1):
            num = arr[i]
            if num + difference in numDict:
                numDict[num] = numDict[num+difference] + 1
                ret = max(ret, numDict[num])
            else:
                numDict[num] = 1
        return ret
