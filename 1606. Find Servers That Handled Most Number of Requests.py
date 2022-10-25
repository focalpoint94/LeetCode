from sortedcontainers import SortedList
from bisect import bisect_left
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        # (finishTime, serverID)
        schedules = []
        # serverID
        idleServers = SortedList(list(range(k)))
        # current time
        curTime = 0
        # workLoads
        workLoads = [0] * k
        
        for i, (t, l) in enumerate(zip(arrival, load)):
            
            curTime = t
            while schedules and schedules[0][0] <= curTime:
                _, serverID = heapq.heappop(schedules)
                idleServers.add(serverID)
            
            if not idleServers:
                continue
                
            num = i % k
            idx = bisect_left(idleServers, num)
            if idx < len(idleServers):
                serverID = idleServers[idx]
            else:
                serverID = idleServers[0]
            heapq.heappush(schedules, (curTime+l, serverID))
            idleServers.discard(serverID)
            workLoads[serverID] += 1
         
        maxLoad = max(workLoads)
        return [i for i in range(k) if workLoads[i] == maxLoad]
