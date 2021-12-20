class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        order = 1
        for char in columnTitle[::-1]:
            ret += order * (ord(char) - 64)
            order *= 26
        return ret
