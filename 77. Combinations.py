class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret = []
        self.helper([i+1 for i in range(n)], k, [])
        return self.ret
        
    def helper(self, nums, k, path):
        if k == 0:
            self.ret.append(path)
            return
        for i, num in enumerate(nums):
            self.helper(nums[i+1:], k-1, path+[num])
