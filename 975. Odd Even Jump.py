class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)
        oddNext, stack = [None] * N, []
        for val, idx in sorted([(val, idx) for idx, val in enumerate(arr)]):
            while stack and stack[-1] < idx:
                oddNext[stack.pop()] = idx
            stack.append(idx)
        evenNext, stack = [None] * N, []
        for val, idx in sorted([(-val, idx) for idx, val in enumerate(arr)]):
            while stack and stack[-1] < idx:
                evenNext[stack.pop()] = idx
            stack.append(idx)
        
        oddCanReach = [False] * N
        evenCanReach = [False] * N
        oddCanReach[-1] = evenCanReach[-1] = True
        
        for i in range(N-2, -1, -1):
            if oddNext[i] is not None:
                oddCanReach[i] = evenCanReach[oddNext[i]]
            if evenNext[i] is not None:
                evenCanReach[i] = oddCanReach[evenNext[i]]
        
        return sum(oddCanReach)
