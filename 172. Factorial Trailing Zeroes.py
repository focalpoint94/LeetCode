class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        x = 5
        while n >= x:
            ret += n // x
            x *= 5
        return ret
