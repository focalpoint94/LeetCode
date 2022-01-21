class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m, n = len(matrix), len(matrix[0])
        
        row = 0
        # row search
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                row = max(row, mid)
                l = mid + 1
        
        # column search
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
