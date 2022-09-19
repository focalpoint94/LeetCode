from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for val in sorted(arr, key=abs):
            if c[val] == 0:
                continue
            if c[val*2] == 0:
                return False
            c[val] -= 1
            c[val*2] -= 1
        return True
