from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        ret = 0
        charSet, counter = set(), Counter()
        i = 0
        for j in range(len(s)):
            charSet.add(s[j])
            counter[s[j]] += 1
            if len(charSet) == k + 1:
                while len(charSet) == k + 1:
                    counter[s[i]] -= 1
                    if counter[s[i]] == 0:
                        charSet.remove(s[i])
                    i += 1
            ret = max(ret, j-i+1)
        return ret                
