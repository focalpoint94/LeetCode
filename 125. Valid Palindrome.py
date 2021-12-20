import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s.strip()
        if not s:
            return True
        ss = ''
        i = 0
        p = re.compile('[a-z0-9]')
        while i < len(s):
            if p.match(s[i]):
                ss += s[i]
            i += 1
        return ss == ss[::-1]
