class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        nSet, val = set([1]), 1
        for x in range(31):
            val *= 2
            nSet.add(val)
        return n in nSet
