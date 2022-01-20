class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        b = '0'*(len(a)-len(b)) + b
        ret = ''
        carry = 0
        for i in range(len(a)-1, -1, -1):
            temp = int(a[i]) + int(b[i]) + carry
            ret += str(temp%2)
            carry = temp//2
        if carry:
            ret += str(1)
        return ret[::-1]
