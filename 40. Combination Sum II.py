class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ret = []
        self.dfs(candidates, target, [])
        return self.ret
        
    def dfs(self, candidates, target, path):
        if target < 0:
            return
        if target == 0:
            self.ret.append(path)
            return
        prev = None
        for i, candidate in enumerate(candidates):
            if candidate != prev:
                prev = candidate
                self.dfs(candidates[i+1:], target-candidate, path+[candidate])
