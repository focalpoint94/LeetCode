class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        ret, cur = [], 2
        while cur < finalSum // 2:
            finalSum -= cur
            ret.append(cur)
            cur += 2
        ret.append(finalSum)
        return ret
