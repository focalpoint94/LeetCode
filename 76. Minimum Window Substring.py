class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        need, missing = Counter(t), len(t)
        i, start, end = 0, 0, 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j - i < end - start:
                    end, start = j, i
                need[s[i]] += 1
                missing += 1
                i += 1
        return s[start:end]
