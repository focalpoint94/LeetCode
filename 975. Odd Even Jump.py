class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        oddNext = [None] * n
        evenNext = [None] * n
        stack = []
        for val, idx in sorted([(val, idx) for idx, val in enumerate(arr)]):
            while stack and stack[-1] < idx:
                oddNext[stack.pop()] = idx
            stack.append(idx)
        stack = []
        for val, idx in sorted([(-val, idx) for idx, val in enumerate(arr)]):
            while stack and stack[-1] < idx:
                evenNext[stack.pop()] = idx
            stack.append(idx)
        
        oddCanReach = [False] * n
        evenCanReach = [False] * n
        oddCanReach[-1] = True
        evenCanReach[-1] = True
        
        for idx in range(n-2, -1, -1):
            if oddNext[idx] != None:
                oddCanReach[idx] = evenCanReach[oddNext[idx]]
            if evenNext[idx] != None:
                evenCanReach[idx] = oddCanReach[evenNext[idx]]
        
        return sum(oddCanReach)
