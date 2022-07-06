class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            x = 3
            while n >= x:
                if n % x != 0:
                    return False
                n /= x
                x *= 3
        return n == 1
