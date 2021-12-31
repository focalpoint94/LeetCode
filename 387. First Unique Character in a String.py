from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        candidates = set()
        for k, v in c.items():
            if v == 1:
                candidates.add(k)
        if not candidates:
            return -1
        for i, char in enumerate(s):
            if char in candidates:
                return i
