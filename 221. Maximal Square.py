class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ret = 0
        if '1' in matrix[0] or '1' in [r[0] for r in matrix]:
            ret = 1
        m, n = len(matrix), len(matrix[0])
        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][x] == '1':
                    matrix[y][x] = str(min(int(matrix[y-1][x-1]), int(matrix[y-1][x]), int(matrix[y][x-1])) + 1)
                    ret = max(ret, int(matrix[y][x])*int(matrix[y][x]))
        return ret
