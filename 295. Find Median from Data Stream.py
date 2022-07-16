import heapq
class MedianFinder:

    def __init__(self):
        self.size = 0
        # self.h1: max heap containing the small half
        # self.h2: min heap containing the large half
        self.h1, self.h2 = [], []
    
    def addNum(self, num: int) -> None:
        self.size += 1
        if self.size % 2 == 1:
            if not self.h1 or num <= self.h2[0]:
                heapq.heappush(self.h1, -num)
            else:
                heapq.heappush(self.h1, -heapq.heappushpop(self.h2, num))
        else:
            if num <= -self.h1[0]:
                heapq.heappush(self.h2, -heapq.heappushpop(self.h1, -num))
            else:
                heapq.heappush(self.h2, num)

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.h1[0] + self.h2[0])/2.
        else:
            return -self.h1[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
