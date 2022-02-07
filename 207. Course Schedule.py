class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
        q = []
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(node)
        
        while q:
            u = q.pop()
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        
        for node, indegree in enumerate(indegrees):
            if indegree != 0:
                return False
        return True
