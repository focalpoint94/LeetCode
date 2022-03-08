class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        ret = []
        
        TaskHeap = []
        WaitHeap = []
        
        for idx, task in enumerate(tasks):
            heapq.heappush(TaskHeap, (task[0], idx, task[1]))
            
        curTime = 0
        while True:
            
            if not WaitHeap:
                if not TaskHeap:
                    break                
                startTime, idx, processTime = heapq.heappop(TaskHeap)
                heapq.heappush(WaitHeap, (processTime, idx, startTime))
                while TaskHeap and TaskHeap[0][0] == startTime:
                    startTime, idx, processTime = heapq.heappop(TaskHeap)
                    heapq.heappush(WaitHeap, (processTime, idx, startTime))
                curTime = startTime
            
            processTime, idx, startTime = heapq.heappop(WaitHeap)
            ret.append(idx)
            curTime += processTime
            
            while TaskHeap and TaskHeap[0][0] <= curTime:
                startTime, idx, processTime = heapq.heappop(TaskHeap)
                heapq.heappush(WaitHeap, (processTime, idx, startTime))
        
        return ret
