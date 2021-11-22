class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)
        self.ret = []
        self.dfs(s, [])
        return self.ret
    
    def dfs(self, s, path):
        if not s:
            self.ret.append(" ".join(path))
            return
        for i in range(1, len(s)+1):
            if s[:i] in self.wordDict:
                self.dfs(s[i:], path+[s[:i]])
