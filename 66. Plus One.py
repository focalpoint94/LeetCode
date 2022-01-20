class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        ret.append((digits[-1] + 1) % 10)
        carry = (digits[-1] + 1) // 10
        for digit in reversed(digits[:-1]):
            ret.append((digit + carry) % 10)
            carry = (digit + carry) // 10
        if carry == 1:
            ret.append(1)
        return reversed(ret)
