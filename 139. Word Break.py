class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        self.dp = set()
        return self.dfs(s)
        
    def dfs(self, s):
        if not s:
            return True
        if s in self.dp:
            return False
        for i in range(1, len(s)+1):
            if s[:i] in self.wordDict:
                if self.dfs(s[i:]):
                    return True
        self.dp.add(s)
        return False
