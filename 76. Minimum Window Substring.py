from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        ret = ''
        counter, charSet = Counter(t), set(t)        
        j = 0
        for i, c in enumerate(s):
            counter[c] -= 1
            if c in charSet and counter[c] == 0:
                charSet.remove(c)
            while j < i and counter[s[j]] < 0:
                counter[s[j]] += 1
                j += 1
            if not charSet:
                if not ret or len(ret) > i - j + 1:
                    ret = s[j:i+1]
        return ret
