class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        INF = int(1e9)
        distance = [INF] * (n+1)
        graph = [[] for _ in range(n+1)]
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        pq = [(0, k)]
        distance[k] = 0
        while pq:
            dist_u, u = heapq.heappop(pq)
            if dist_u > distance[u]:
                continue
            for v, dist_uv in graph[u]:
                if distance[v] > dist_u + dist_uv:
                    distance[v] = dist_u + dist_uv
                    heapq.heappush(pq, (distance[v], v))
        
        return max(distance[1:]) if max(distance[1:]) != INF else -1
