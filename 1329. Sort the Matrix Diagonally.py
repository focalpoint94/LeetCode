class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        starting_points = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        for starting_point in starting_points:
            array = []
            y, x = starting_point
            while y <= m - 1 and x <= n - 1:
                array.append(mat[y][x])
                y += 1
                x += 1
            array.sort()
            y, x = starting_point
            for val in array:
                mat[y][x] = val
                y += 1
                x += 1
        return mat
