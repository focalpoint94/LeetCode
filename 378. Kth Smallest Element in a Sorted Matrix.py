class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        def count(mid):
            cnt = 0
            y, x = 0, m - 1
            while y <= m - 1 and x >= 0:
                if matrix[y][x] <= mid:
                    cnt += x + 1
                    y += 1
                else:
                    x -= 1
            return cnt
        
        left, right = matrix[0][0], matrix[m-1][m-1]
        ret = matrix[m-1][m-1]
        while left <= right:
            mid = (left + right) // 2
            cnt = count(mid)
            if cnt < k:
                left = mid + 1
            else:
                ret = min(ret, mid)
                right = mid - 1
        return ret
