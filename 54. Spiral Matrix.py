class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.ret = []
        self.helper(matrix, 0, 0, len(matrix), len(matrix[0]))
        return self.ret
        
    def helper(self, matrix, y, x, m, n):
        if m > 0:
            for i in range(n):
                self.ret.append(matrix[y][x])
                x += 1
            x -= 1
            m -= 1
        if n > 0 :
            for i in range(m):
                y += 1
                self.ret.append(matrix[y][x])
            n -= 1
        if m > 0:
            for i in range(n):
                x -= 1
                self.ret.append(matrix[y][x])
            m -= 1
        if n > 0:
            for i in range(m):
                y -= 1
                self.ret.append(matrix[y][x])
            n -= 1
        if m > 0 and n > 0:
            self.helper(matrix, y, x+1, m, n)
