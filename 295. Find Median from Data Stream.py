class MedianFinder:
    import heapq
    
    def __init__(self):
        self.h1 = []
        self.h2 = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        if self.count % 2 == 1:
            if not self.h1 or num <= self.h2[0]:
                heapq.heappush(self.h1, -num)
            else:
                heapq.heappush(self.h1, -heapq.heappushpop(self.h2, num))
        else:
            if num >= -self.h1[0]:
                heapq.heappush(self.h2, num)
            else:
                heapq.heappush(self.h2, -heapq.heappushpop(self.h1, -num))            
    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return -self.h1[0]
        return (-self.h1[0] + self.h2[0])/2.   


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
