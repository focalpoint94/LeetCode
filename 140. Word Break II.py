class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)
        self.ret = []
        self.dfs(s, [])
        return self.ret
        
    def dfs(self, s, path):
        if not s:
            self.ret.append(' '.join(path))
            return
        for word in self.wordDict:
            k = len(word)
            if s[:k] == word:
                self.dfs(s[k:], path+[word])
