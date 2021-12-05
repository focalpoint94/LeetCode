class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        charSet = set()
        j = 0
        ret = 0
        for i in range(len(s)):
            if s[i] not in charSet:
                charSet.add(s[i])
            else:
                while s[i] in charSet:
                    charSet.remove(s[j])
                    j += 1
                charSet.add(s[i])
            ret = max(ret, i - j + 1)
        return ret
