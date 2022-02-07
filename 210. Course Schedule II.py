class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
            
        ret = []
        q = []
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(node)
        
        while q:
            u = q.pop()
            ret.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        
        return ret if len(ret) == numCourses else []
