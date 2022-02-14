class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        turns = [0] * n
        
        for u, v, p in flights:
            graph[u].append((v, p))
        
        import heapq
        pq = [(0, src, k+1)]
        
        while pq:
            price_u, u, turn = heapq.heappop(pq)
            turns[u] = turn
            if u == dst:
                return price_u
            if turn == 0:
                continue
            for v, p in graph[u]:
                if turn - 1 >= turns[v]:
                    heapq.heappush(pq, (price_u+p, v, turn-1))
        return -1
