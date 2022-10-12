import heapq
from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        ret = []
        tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        tasks.sort()
        tasks = deque(tasks)
        
        # q for cpu
        # (processingTime, idx)
        q = []
        t = 0
        while len(ret) < N:
            while tasks:
                enqueueTime, processingTime, idx = tasks.popleft()
                if enqueueTime <= t:
                    heapq.heappush(q, (processingTime, idx))
                else:
                    tasks.appendleft((enqueueTime, processingTime, idx))
                    break
            if q:
                processingTime, idx = heapq.heappop(q)
                t += processingTime
                ret.append(idx)
            else:
                t = tasks[0][0]
        return ret
