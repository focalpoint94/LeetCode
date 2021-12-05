class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrime = [True] * n
        
        p = 2
        while p * p <= n:
            if isPrime[p]:
                q = p * p
                while q < n:
                    isPrime[q] = False
                    q += p
            p += 1
        
        ret = 0
        for i in range(2, n):
            if isPrime[i]:
                ret += 1
        return ret
