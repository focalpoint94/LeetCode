class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.visited = set()
        return self.dfs(s)
        
    def dfs(self, s):
        if not s:
            return True
        if s in self.visited:
            return False
        for word in self.wordDict:
            k = len(word)
            if s[:k] == word:
                if self.dfs(s[k:]):
                    return True
        self.visited.add(s)
        return False
