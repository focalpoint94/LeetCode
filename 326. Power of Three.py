class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            d = 3
            while n >= d:
                if n % d != 0:
                    return False
                n /= d
                d *= 3
        return (n == 1)
