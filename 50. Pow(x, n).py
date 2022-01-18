class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1:
            return 1
        if x == -1:
            if abs(n) % 2 == 0:
                return 1
            else:
                return -1
        if x == 0:
            return 0
        
        n_sign = True if n > 0 else False
        
        res = 1
        count = 0
        
        while count < abs(n):
            multiplier = x
            step = 1
            while step <= abs(n) - count:
                res *= multiplier
                count += step
                step *= 2
                multiplier *= multiplier
                
        if n_sign:
            return res
        
        return 1 / res
        
        
