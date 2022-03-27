class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1] * n for n in range(1, rowIndex+2)]
        for row in range(2, rowIndex+1):
            for col in range(1, row):
                rows[row][col] = rows[row-1][col-1] + rows[row-1][col]
        return rows[-1]
