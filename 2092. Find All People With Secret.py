
'''
BFS Solution - 1
'''

from collections import defaultdict, deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        meetings.append([0, firstPerson, 10**5+1])
        
        knowing, graph = set([0, firstPerson]), defaultdict(set)
        processing = set()
        prevTime = 0
        
        for x, y, t in meetings:
            # new time
            if t != prevTime:
                processing = deque(processing)
                while processing:
                    u = processing.popleft()
                    for v in graph[u]:
                        if v not in knowing:
                            knowing.add(v)
                            processing.append(v)
                graph = defaultdict(set)
                processing = set()
                prevTime = t
            graph[x].add(y)
            graph[y].add(x)
            if x in knowing: processing.add(x)
            if y in knowing: processing.add(y)
        return knowing

    
    
'''
BFS Solution - 2
'''

from collections import defaultdict, deque
from itertools import groupby

class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        knowing = set([0, firstPerson])
        for _, group in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            q = set()
            graph = defaultdict(set)
            for x, y, t in group:
                graph[x].add(y)
                graph[y].add(x)
                if x in knowing: q.add(x)
                if y in knowing: q.add(y)
            
            q = deque(q)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in knowing:
                        knowing.add(v)
                        q.append(v)
        return knowing
