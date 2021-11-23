class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.graph = [[] for _ in range(n)]
        self.connections_set = set()
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.connections_set.add((u, v))
        visited = [False] * n
        self.ret = 0
        self.dfs(0, visited)
        return self.ret
        
    def dfs(self, node, visited):
        visited[node] = True
        for v in self.graph[node]:
            if not visited[v]:
                if (node, v) in self.connections_set:
                    self.ret += 1
                self.dfs(v, visited)
