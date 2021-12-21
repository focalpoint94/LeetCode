class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(x):
            ret = 0
            while x > 0:
                ret += (x % 10)**2
                x //= 10
            return ret
        
        numSet = set([n])
        x = n
        while True:
            x = calc(x)
            if x == 1:
                return True
            if x in numSet:
                return False
            numSet.add(x)
        
