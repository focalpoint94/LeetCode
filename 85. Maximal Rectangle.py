class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ret = 0
        m, n = len(matrix), len(matrix[0])
        heights = [[0] * (n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[i][j] = heights[i-1][j] + 1
                else:
                    heights[i][j] = 0
        for i in range(m):
            stack = [-1]
            for j, h in enumerate(heights[i]):
                if len(stack) == 1 or h >= heights[i][stack[-1]]:
                    stack.append(j)
                else:
                    while len(stack) >= 1 and heights[i][stack[-1]] > h:
                        k = stack.pop()
                        ret = max(ret, (j-stack[-1]-1)*heights[i][k])
                    stack.append(j)
        return ret
