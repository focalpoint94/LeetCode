class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums, path):
        if not nums:
            self.ret.append(path)
            return
        
        prev = None
        for i, num in enumerate(nums):
            if num != prev:
                self.dfs(nums[:i]+nums[i+1:], path+[num])
                prev = num
