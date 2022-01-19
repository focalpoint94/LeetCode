class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0] * n for _ in range(n)]
        num = 1
        count = 0
        y, x = count, count
        while y < n:
            y, x = count, count
            i, j = y, x
            for j in range(x, n):
                ret[i][j] = num
                num += 1
            for i in range(y+1, n):
                ret[i][j] = num
                num += 1
            for j in range(n-2, x-1, -1):
                ret[i][j] = num
                num += 1
            for i in range(n-2, y, -1):
                ret[i][j] = num
                num += 1
            count += 1
            n -= 1
        return ret
