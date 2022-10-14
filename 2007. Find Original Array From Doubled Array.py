from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        ret = []
        c = Counter(changed)
        
        changed.sort()
        for num in changed:
            if c[num] == 0:
                continue
            
            if c[num*2] == 0:
                return []
            
            c[num] -= 1
            c[num*2] -= 1
            ret.append(num)
            
        return ret
