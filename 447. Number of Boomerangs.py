class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        from collections import Counter
        
        def dist(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        
        ret = 0
        for i in range(len(points)):
            p1 = points[i]
            c = Counter()
            for j in range(len(points)):
                p2 = points[j]
                c[dist(p1, p2)] += 1
            for k, v in c.items():
                if v >= 2:
                    ret += v * (v-1)
        return ret
