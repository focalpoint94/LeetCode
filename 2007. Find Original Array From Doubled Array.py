class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import Counter
        ret = []
        changed.sort()
        c = Counter(changed)
        for num in changed:
            if c[num] != 0:
                c[num] -= 1
                ret.append(num)
                if c[num*2] == 0:
                    return []
                c[num*2] -= 1
        return ret
