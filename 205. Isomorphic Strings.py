class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for idx in range(len(s)):
            c1, c2 = s[idx], t[idx]
            if c1 in dic1 and dic1[c1] != c2:
                return False
            if c2 in dic2 and dic2[c2] != c1:
                return False
            dic1[c1] = c2
            dic2[c2] = c1
        return True
