class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums, path):
        self.ret.append(path)
        prev = None
        for i, num in enumerate(nums):
            if num != prev:
                prev = num
                self.dfs(nums[i+1:], path+[num])
