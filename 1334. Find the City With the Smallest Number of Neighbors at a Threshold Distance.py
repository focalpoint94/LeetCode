class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = int(1e9)
        graph = [[INF] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        
        for u, v, d in edges:
            graph[u][v] = d
            graph[v][u] = d
        
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    graph[u][v] = min(graph[u][v], graph[u][k]+graph[k][v])
        
        ret, reg = 0, -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if graph[i][j] > distanceThreshold:
                    cnt += 1
            if cnt >= reg:
                ret, reg = i, cnt
        return ret
        
        
