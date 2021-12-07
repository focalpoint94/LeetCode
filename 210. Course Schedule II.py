from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree_list = [0] * numCourses
        
        for v, u in prerequisites:
            graph[u].append(v)
            indegree_list[v] += 1
        
        result = []
        q = deque()
        for i in range(numCourses):
            if indegree_list[i] == 0:
                q.append(i)
        
        while q:
            now = q.popleft()
            result.append(now)
            for nxt in graph[now]:
                indegree_list[nxt] -= 1
                if indegree_list[nxt] == 0:
                    q.append(nxt)
        
        if len(result) == numCourses:
            return result
        return []
