from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        dic = defaultdict(list)
        for i, num in enumerate(arr):
            dic[num].append(i)
        
        # (idx, turn)
        q = deque()
        q.append((0, 0))
        
        # visited idx
        visited = set()
        visited.add(0)
        
        while q:
            i, t = q.popleft()
            if i == len(arr) - 1:
                return t
            # adjacents
            if i - 1 >= 0 and i - 1 not in visited:
                q.append((i-1, t+1))
                visited.add(i - 1)
            if i + 1 <= len(arr) - 1 and i + 1 not in visited:
                q.append((i+1, t+1))
                visited.add(i + 1)
            # jumps
            for j in dic[arr[i]]:
                if j != i and j not in visited:
                    q.append((j, t+1))
                    visited.add(j)
            # remove
            dic.pop(arr[i])
            
