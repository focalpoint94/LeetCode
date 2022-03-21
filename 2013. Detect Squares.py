class DetectSquares:
    from collections import Counter
    def __init__(self):
        self.counter = Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ret = 0
        for candidate, freq in self.counter.items():
            x1, y1 = point
            x2, y2 = candidate
            if x1 == x2 or y1 == y2 or abs(x1 - x2) != abs(y1 - y2):
                continue
            if (x1, y2) in self.counter and (x2, y1) in self.counter:
                ret += freq * self.counter[(x1, y2)] * self.counter[(x2, y1)]
        return ret

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
