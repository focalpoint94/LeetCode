import heapq 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        distance = [float('inf')] * (n+1)
        distance[0] = distance[k] = 0
        
        h = [(k, 0)]
        while h:
            u, dist_u = heapq.heappop(h)
            if dist_u > distance[u]:
                continue
            for v, dist_uv in graph[u]:
                if distance[v] > dist_u + dist_uv:
                    distance[v] = dist_u + dist_uv
                    heapq.heappush(h, (v, distance[v]))
        return -1 if max(distance) == float('inf') else max(distance)
