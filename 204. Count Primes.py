class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = 0
        p = 2
        while p * p <= n:
            if isPrime[p]:
                q = p * p
                while q < n:
                    isPrime[q] = False
                    q += p
            p += 1
        return sum(isPrime)
