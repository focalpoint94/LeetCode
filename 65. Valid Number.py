class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        pat = re.compile('(^[+-]?((\d+(\.\d*)?)|(\.\d+))$)|(^[+-]?((\d+(\.\d*)?)|(\.\d+))[eE][+-]?\d+$)')
        return re.match(pat, s)
