class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        ref1 = grid[0]
        ref2 = [x^1 for x in grid[0]]
        for row in grid:
            if row != ref1 and row != ref2:
                return False
        return True
