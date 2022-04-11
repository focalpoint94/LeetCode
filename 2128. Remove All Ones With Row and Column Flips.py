class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        samples = [grid[0], [x^1 for x in grid[0]]]
        for i in range(1, len(grid)):
            if grid[i] not in samples:
                return False
        return True        
