class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        h = []
        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                heapq.heappush(h, num)
                heapq.heappop(h)
        return h[0]
