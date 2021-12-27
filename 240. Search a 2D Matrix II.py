class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = bisect_right(matrix[0], target) - 1
        i = bisect_right([mat[0] for mat in matrix], target) - 1
        while i >= 0 and j >= 0:
            if matrix[i][j] < target:
                return False
            for k in range(0, i+1):
                if matrix[k][j] == target:
                    return True
            for k in range(0, j+1):
                if matrix[i][k] == target:
                    return True
            i -= 1
            j -= 1
