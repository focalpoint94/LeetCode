class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(x):
            if x == 1:
                return 1
            return x * fact(x-1)
        
        k -= 1
        s = ''
        candidates = [i+1 for i in range(n)]
        for i in range(n-1):
            divisor = fact((len(candidates) - 1))
            quotient = k // divisor
            s += str(candidates[quotient])
            k -= divisor * quotient
            candidates.remove(candidates[quotient])
        s += str(candidates[0])
        return s
