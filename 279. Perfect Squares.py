class Solution:
    def numSquares(self, n):
        self.PSN = set([i*i for i in range(1, int(n**0.5)+1)])
        for h in range(1, n+1):
            if self.helper(n, h):
                return h
    
    def helper(self, n, depth):
        if depth == 1:
            return n in self.PSN
        
        for x in self.PSN:
            if self.helper(n-x, depth-1):
                return True
        return False
