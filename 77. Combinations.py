class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        nums = [i for i in range(1, n+1)]
        
        def backtrack(nums, path):
            nonlocal k
            if len(path) == k:
                ret.append(path)
                return
            
            for i, num in enumerate(nums):
                backtrack(nums[i+1:], path+[nums[i]])
        
        backtrack(nums, [])
        return ret
