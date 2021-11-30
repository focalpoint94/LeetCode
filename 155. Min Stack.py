import heapq
class MinStack:

    def __init__(self):
        self.stack = []
        self.h = []
        self.p = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.h, val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.h[0]:
            heapq.heappop(self.h)
            while self.h and self.p and self.h[0] == self.p[0]:
                heapq.heappop(self.h)
                heapq.heappop(self.p)
        else:
            heapq.heappush(self.p, val)
        return val
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.h[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
