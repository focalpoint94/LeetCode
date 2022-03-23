import heapq

class MyHeap:
    def __init__(self, type='min'):
        self.heap = []
        self.removals = []
        self.sign = 1 if type == 'min' else -1

    def insert(self, elem):
        heapq.heappush(self.heap, self.sign * elem)

    def __getitem__(self, idx):
        return self.sign * self.heap[idx]

    def __len__(self):
        return len(self.heap) - len(self.removals)

    def remove(self, elem):
        if elem == self.sign * self.heap[0]:
            heapq.heappop(self.heap)
            while self.removals and self.heap[0] == self.removals[0]:
                heapq.heappop(self.heap)
                heapq.heappop(self.removals)
        else:
            heapq.heappush(self.removals, self.sign * elem)


class StockPrice:
    
    def __init__(self):
        # data[timestamp] = price
        self.data = {}
        self.maxtimestamp = -1
        self.maxheap = MyHeap('max')
        self.minheap = MyHeap('min')

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.data:
            wrong_price = self.data[timestamp]            
            self.maxheap.remove(wrong_price)
            self.minheap.remove(wrong_price)
        self.data[timestamp] = price
        self.maxtimestamp = max(self.maxtimestamp, timestamp)
        self.maxheap.insert(price)
        self.minheap.insert(price)
        
    def current(self) -> int:
        return self.data[self.maxtimestamp]

    def maximum(self) -> int:
        return self.maxheap[0]
    
    def minimum(self) -> int:
        return self.minheap[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
