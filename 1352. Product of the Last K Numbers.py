class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        self.lastZeroIdx = -1
        self.idx = -1

    def add(self, num: int) -> None:
        self.idx += 1
        if num == 0:
            self.lastZeroIdx = self.idx
            self.product.append(self.product[-1])
        else:
            self.product.append(self.product[-1]*num)
        
    def getProduct(self, k: int) -> int:
        if self.lastZeroIdx < self.idx - k + 1:
            return int(self.product[-1] / self.product[self.idx-k+1])
        else:
            return 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
