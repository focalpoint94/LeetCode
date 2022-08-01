from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        ret = []
        h = [(-f, c)for c, f in Counter(s).items()]
        heapq.heapify(h)
        
        while len(h) > 1:
            f1, c1 = heapq.heappop(h)
            f2, c2 = heapq.heappop(h)
            f1, f2 = -f1, -f2
            ret.append(c1)
            ret.append(c2)
            if f1 >= 2:
                heapq.heappush(h, (-f1+1, c1))
            if f2 >= 2:
                heapq.heappush(h, (-f2+1, c2))
            
        if h:
            f, c = h[0]
            if abs(f) >= 2:
                return ""
            ret.append(c)
        return ''.join(ret)
