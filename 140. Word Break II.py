class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordSet = wordDict
        self.ret = []
        self.backtrack(s, [])
        return self.ret
        
    def backtrack(self, s, path):
        if not s:
            self.ret.append(' '.join(path))
            return
        
        for word in self.wordSet:
            k = len(word)
            if s[:k] == word:
                self.backtrack(s[k:], path+[word])
