class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        from collections import defaultdict
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        chars = set()
        for key, val in dic.items():
            if val < k:
                chars.add(key)
        if not chars:
            return len(s)
        indexs = []
        for i, c in enumerate(s):
            if c in chars:
                indexs.append(i)
        ret = 0
        prev = 0
        for idx in indexs:
            ns = s[prev:idx]
            ret = max(ret, self.longestSubstring(ns, k))
            prev = idx+1
        ns = s[prev:]
        ret = max(ret, self.longestSubstring(ns, k))
        return ret
