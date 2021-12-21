class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret += n & 1
            n >>= 1
        return ret
