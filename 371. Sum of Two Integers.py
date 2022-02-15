class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if y > x:
            return self.getSum(b, a)
        sign = 1 if a >= 0 else -1
        if a * b >= 0:
            while y:
                temp, carry = (x ^ y), (x & y) << 1
                x, y = temp, carry
        else:
            while y:
                temp, borrow = (x ^ y), ((~x) & y) << 1
                x, y = temp, borrow
        return sign * x
