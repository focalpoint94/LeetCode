class WordFilter:

    def __init__(self, words: List[str]):
        wordDict = {}
        for idx, word in enumerate(words):
            wordDict[word] = idx
        self.PrefixTree = {}
        self.SuffixTree = {}
        
        for word, idx in wordDict.items():
            node = self.PrefixTree
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
                if 'IdxList' not in node:
                    node['IdxList'] = []
                node['IdxList'].append(idx)
            node['#'] = '#'
            
            node = self.SuffixTree
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
                if 'IdxList' not in node:
                    node['IdxList'] = []
                node['IdxList'].append(idx)
            node['#'] = '#'
                
                
    def f(self, prefix: str, suffix: str) -> int:
        node = self.PrefixTree
        for c in prefix:
            if c not in node:
                return -1
            node = node[c]
        PrefixMatchList = node['IdxList']
        
        node = self.SuffixTree
        for c in suffix[::-1]:
            if c not in node:
                return -1
            node = node[c]
        SuffixMatchList = node['IdxList']
        
        MatchList = list(set(PrefixMatchList) & set(SuffixMatchList))
        return -1 if not MatchList else max(MatchList)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
