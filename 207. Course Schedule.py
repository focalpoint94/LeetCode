from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
        
        cnt = 0
        q = deque([u for u in range(numCourses) if indegrees[u] == 0])
        while q:
            u = q.popleft()
            cnt += 1
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return cnt == numCourses
