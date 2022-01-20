class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    self.inspect_row(matrix, y, x)
                    self.inspect_column(matrix, y, x)
                elif matrix[y][x] == 'row inspected zero':
                    self.inspect_column(matrix, y, x)
                elif matrix[y][x] == 'column inspected zero':
                    self.inspect_row(matrix, y, x)
                else:
                    continue
        for y in range(m):
            for x in range(n):
                if type(matrix[y][x]) != int:
                    matrix[y][x] = 0
        
    def inspect_row(self, matrix, y, x):
        for i in range(len(matrix[0])):
            cur = matrix[y][i]
            if cur == 0:
                matrix[y][i] = 'row inspected zero'
            elif cur == 'row inspected zero':
                continue
            elif cur == 'column inspected zero':
                matrix[y][i] = 'both inspected zero'
            elif cur == 'both inspected zero':
                continue
            else:
                matrix[y][i] = 'to be zero'
    
    def inspect_column(self, matrix, y, x):
        for i in range(len(matrix)):
            cur = matrix[i][x]
            if cur == 0:
                matrix[i][x] = 'column inspected zero'
            elif cur == 'row inspected zero':
                matrix[i][x] = 'both inspected zero'
            elif cur == 'column inspected zero':
                continue
            elif cur == 'both inspected zero':
                continue
            else:
                matrix[i][x] = 'to be zero'
