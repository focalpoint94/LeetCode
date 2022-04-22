
'''
TLE
'''

from collections import defaultdict
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        meetings.append([0, firstPerson, 10**5+1])
        
        knowing, graph = set([0, firstPerson]), defaultdict(set)
        prevTime = 0
        
        for x, y, t in meetings:
            # new time
            if t != prevTime:
                processing, processed = list(knowing), set(knowing)
                while processing:
                    u = processing.pop()
                    processed.add(u)
                    for v in graph[u]:
                        knowing.add(v)
                        if v not in processed:
                            processing.append(v)
                graph = defaultdict(set)
                prevTime = t
            graph[x].add(y)
            graph[y].add(x)
        return list(knowing)
