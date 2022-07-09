class Solution:
    def numSquares(self, n: int) -> int:
        PSNs = set([i*i for i in range(1, int(n**0.5)+1)])
        
        def iddfs(n, h):
            if h == 1:
                return n in PSNs
            for PSN in PSNs:
                if iddfs(n-PSN, h-1):
                    return True
            return False
        
        for h in range(1, n+1):
            if iddfs(n, h):
                return h
            
            
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        PSNs = set([i*i for i in range(1, int(n**0.5)+1)])
        q = deque()
        q.append((n, 0))
        while q:
            n, t = q.popleft()
            for PSN in PSNs:
                if PSN == n:
                    return t + 1
                if PSN < n:
                    q.append((n-PSN, t+1))
