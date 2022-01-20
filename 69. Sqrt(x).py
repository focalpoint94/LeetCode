class Solution:
    def mySqrt(self, x: int) -> int:
        ret = 0
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > x:
                r = mid - 1
            else:
                ret = max(ret, mid)
                l = mid + 1
        return ret
