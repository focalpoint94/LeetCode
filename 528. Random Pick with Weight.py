class Solution:
    import random
    def __init__(self, w: List[int]):
        self.cumulative = []
        summed = 0
        for val in w:
            summed += val
            self.cumulative.append(summed)

    def pickIndex(self) -> int:
        ret = len(self.cumulative) - 1
        rand = random.randint(1, self.cumulative[-1])
        left, right = 0, len(self.cumulative) - 1
        while left <= right:
            mid = (left + right) // 2
            if rand <= self.cumulative[mid]:
                ret = min(ret, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
