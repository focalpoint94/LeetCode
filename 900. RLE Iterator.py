class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.it = 0
        self.left = self.encoding[0]
        self.length = len(self.encoding)

    def next(self, n: int) -> int:
        consumed = 0
        if n <= self.left:
            self.left -= n
            return self.encoding[self.it+1]
        
        consumed = self.left
        while self.it + 2 <= self.length - 2 and consumed + self.encoding[self.it+2] < n:
            consumed += self.encoding[self.it+2]
            self.it += 2
        
        if self.it == self.length - 2:
            self.left = 0
            return -1
        
        self.it += 2
        consumed += self.encoding[self.it]
        self.left = consumed - n
        return self.encoding[self.it+1]
        
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
