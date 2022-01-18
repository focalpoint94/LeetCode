class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        ret = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                temp = ret[i+j+1] + int(num1[i]) * int(num2[j]) + carry
                carry = temp // 10
                ret[i+j+1] = temp % 10
            ret[i] += carry
        return ''.join(map(str, ret)).lstrip('0')
