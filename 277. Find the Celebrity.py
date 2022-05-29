# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for other in range(n):
            if knows(candidate, other):
                candidate = other
        
        def isCelebrity(candidate):
            for other in range(n):
                if not knows(other, candidate):
                    return False
                if candidate != other and knows(candidate, other):
                    return False
            return True
        
        return candidate if isCelebrity(candidate) else -1
