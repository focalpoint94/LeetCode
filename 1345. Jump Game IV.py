class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        from collections import defaultdict
        # dic[val]: list of index
        dic = defaultdict(list)
        for idx, num in enumerate(arr):
            dic[num].append(idx)    
        
        # visited: visted index
        visited = set([0]) 
        
        ret = 0
        q = [0]
        while q:
            ret += 1
            next_q = []
            for idx in q:
                # left
                if idx - 1 >= 0 and idx - 1 not in visited:
                    visited.add(idx - 1)
                    next_q.append(idx - 1)
                # right
                if idx + 1 <= len(arr) - 1 and idx + 1 not in visited:
                    visited.add(idx + 1)
                    next_q.append(idx + 1)
                    if idx + 1 == len(arr) - 1:
                        return ret
                # same value idx
                for j in dic[arr[idx]]:
                    if j not in visited:
                        visited.add(j)
                        next_q.append(j)
                        if j == len(arr) - 1:
                            return ret
                if arr[idx] in dic:
                    dic.pop(arr[idx])
            q = next_q
        return ret
