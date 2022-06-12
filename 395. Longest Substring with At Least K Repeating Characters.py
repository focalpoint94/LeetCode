from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        
        def helper(s):
            if not s:
                return 0
            counter = Counter(s)
            invalid_chars = set()
            for char, freq in counter.items():
                if freq < k:
                    invalid_chars.add(char)
            if not invalid_chars:
                return len(s)            
            ret, i = 0, 0
            for j in range(len(s)):
                if s[j] in invalid_chars:
                    ret = max(ret, helper(s[i:j]))
                    i = j + 1
            ret = max(ret, helper(s[i:]))
            return ret
        
        return helper(s)
