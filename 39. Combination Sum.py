class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []
        self.dfs(candidates, target, [])
        return self.ret
        
    def dfs(self, candidates, target, path):
        if target < 0:
            return
        if target == 0:
            self.ret.append(path)
            return
        for i, candidate in enumerate(candidates):
            self.dfs(candidates[i:], target-candidate, path+[candidate])
        
