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
    
    
    
    
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         def count(val):
#             cnt = 0
#             y, x = len(matrix[0]) - 1, 0
#             while y >= 0 and x <= len(matrix[0]) - 1:
#                 if matrix[y][x] <= val:
#                     cnt += y + 1
#                     x += 1
#                 else:
#                     y -= 1
#             return cnt
        
#         ret = matrix[-1][-1]
#         left, right = matrix[0][0], matrix[-1][-1]
#         while left <= right:
#             mid = (left + right) // 2
#             if count(mid) < k:
#                 left = mid + 1
#             elif count(mid) >= k:
#                 ret = min(ret, mid)
#                 right = mid - 1
#         return ret
