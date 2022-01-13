class Solution:
    def getSum(self, a: int, b: int) -> int:
        # if b is 0, it doesn't enter while loop
        # in that case, code after while loop doesn't make sense
        if b == 0:
            return a
        
        # bit_mask (32 ones; 1111111..111) is needed to deal with the last 32 bits
        # as python uses infinite number of bits to represent integers
        bit_mask = 0xffffffff
        while b:
            summation = (a ^ b) & bit_mask
            carry = ((a & b) << 1) & bit_mask
            a, b = summation, carry
        
        if (a >> 31) & 1:
            return ~ (a ^ bit_mask)
        return a
