class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        flipFirstRow = False
        flipFirstCol = False
        if matrix[0][0] == 0:
            flipFirstRow, flipFirstCol = True, True
        else:
            for i in range(1, n):
                if matrix[0][i] == 0:
                    flipFirstRow = True
                    break
            for i in range(1, m):
                if matrix[i][0] == 0:
                    flipFirstCol = True
                    break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        if flipFirstRow:
            for i in range(n):
                matrix[0][i] = 0
        
        if flipFirstCol:
            for i in range(m):
                matrix[i][0] = 0
