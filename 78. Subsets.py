class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.helper(nums, [])
        return self.ret
        
    def helper(self, nums, path):
        self.ret.append(path)
        if not nums:
            return
        for i, num in enumerate(nums):
            self.helper(nums[i+1:], path+[num])
