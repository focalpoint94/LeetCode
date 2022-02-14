class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            while y:
                summed = x ^ y
                carry = (x & y) << 1
                x, y = summed, carry
        else:
            while y:
                summed = x ^ y
                borrow = ((~x) & y) << 1
                x, y = summed, borrow
        return x * sign
