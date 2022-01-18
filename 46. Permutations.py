class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums, path):
        if not nums:
            self.ret.append(path)
            return
        for i, num in enumerate(nums):
            self.dfs(nums[:i]+nums[i+1:], path+[num])
