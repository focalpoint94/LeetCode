class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0
        m, n = len(matrix), len(matrix[0])
        for y in range(m):
            for x in range(n):
                if y == 0 or x == 0:
                    ret += matrix[y][x]
                else:
                    if matrix[y][x] != 0:
                        matrix[y][x] = min(matrix[y-1][x], matrix[y][x-1], matrix[y-1][x-1]) + 1                
                        ret += matrix[y][x]
        return ret
