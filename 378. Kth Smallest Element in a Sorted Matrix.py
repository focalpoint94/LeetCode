class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        import heapq
        h = []
        for i in range(n):
            h.append([matrix[i][0], i, 0])
        heapq.heapify(h)
        while k > 0:
            val, row, col = heapq.heappop(h)
            if col != n - 1:
                heapq.heappush(h, [matrix[row][col+1], row, col+1])
            k -= 1
        return val
