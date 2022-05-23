class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.headID, self.manager, self.informTime = headID, manager, informTime
        self.ret = 0
        self.times = [-1] * n
        self.times[headID] = 0
        for idx in range(n):
            if self.times[idx] == -1:
                self.dfs(idx)
        return self.ret
    
    def dfs(self, idx):
        if self.times[idx] != -1:
            return self.times[idx]
        sup = self.manager[idx]
        ret = self.dfs(sup) + self.informTime[sup]
        self.times[idx] = ret
        self.ret = max(self.ret, ret)
        return ret
