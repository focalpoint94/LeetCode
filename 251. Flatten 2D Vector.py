class Vector2D:

    def __init__(self, vec: List[List[int]]):
        def generator(vecs):
            for x in vecs:
                if isinstance(x, list):
                    yield from generator(x)
                else:
                    yield x
        self.g = generator(vec)
        self.val = next(self.g, None)           

    def next(self) -> int:
        ret = self.val
        self.val = next(self.g, None)
        return ret

    def hasNext(self) -> bool:
        return not(self.val is None)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
