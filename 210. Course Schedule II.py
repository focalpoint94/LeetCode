from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
        
        ret = []
        q = deque([u for u in range(numCourses) if indegrees[u] == 0])
        while q:
            u = q.popleft()
            ret.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return ret if len(ret) == numCourses else []
