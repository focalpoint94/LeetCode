class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.graph = [[] for _ in range(n)]
        for u, v in connections:
            self.graph[u].append((v, True))
            self.graph[v].append((u, False))
        self.visited = [False] * n
        self.visited[0] = True
        self.ret = 0
        self.dfs(0)
        return self.ret
        
    def dfs(self, node):
        for v, d in self.graph[node]:
            if not self.visited[v]:
                if d:
                    self.ret += 1
                self.visited[v] = True
                self.dfs(v)
