class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Positive?
        positive = (dividend > 0) is (divisor > 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        subtract = divisor
        while divisor <= dividend:
            subtract, i = divisor, 1
            while subtract <= dividend:
                dividend -= subtract
                res += i
                i <<= 1
                subtract <<= 1
        
        if positive:
            return res
        return -res
                
