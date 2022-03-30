import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = re.compile('([+-]?)([0-9]+)')
        match = re.match(pattern, s.lstrip())
        if not match:
            return 0
        ret = -int(match.group(2)) if match.group(1) == '-' else int(match.group(2))
        if ret <= -2**31:
            ret = -2**31
        elif ret > 2**31 - 1:
            ret = 2 ** 31 - 1
        return ret
