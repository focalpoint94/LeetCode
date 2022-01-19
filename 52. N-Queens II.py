class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ret = 0
        self.helper(n, [i for i in range(n)], [], set(), set())
        return self.ret
    
    def helper(self, n, nums, path, sumset, subset):
        if not nums:
            self.ret += 1
            return
        for i, num in enumerate(nums):
            y, x = n - len(nums), num
            if y + x not in sumset and y - x not in subset:
                sumset.add(y+x)
                subset.add(y-x)
                self.helper(n, nums[:i]+nums[i+1:], path+[num], sumset, subset)
                sumset.remove(y+x)
                subset.remove(y-x)
