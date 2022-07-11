from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        charSet, counter = set(p), Counter(p)
        i = 0
        for j, char in enumerate(s):
            if char not in charSet:
                while i <= j:
                    counter[s[i]] += 1
                    i += 1
            counter[char] -= 1
            if counter[char] < 0:
                while counter[char] < 0:
                    counter[s[i]] += 1
                    i += 1
            if j - i + 1 == len(p):
                ret.append(i)
        return ret
