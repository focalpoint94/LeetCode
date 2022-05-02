class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.wordSet = set(wordList)
        self.wordSet.discard(beginWord)
        if endWord not in self.wordSet: return []
        
        paths, finished = [[beginWord]], False
        while not finished:
            if not paths: return []
            next_paths, visited = [], set()
            while paths:
                path = paths.pop()
                for adjacent in self.adjacents(path[-1]):
                    if adjacent == endWord:
                        finished = True
                    next_paths.append(path+[adjacent])
                    visited.add(adjacent)
            self.wordSet -= visited
            paths = next_paths
        return [path for path in paths if path[-1] == endWord]        
        
    
    def adjacents(self, word):
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(word)):
            for alpha in alphas:
                candidate = word[:i] + alpha + word[i+1:]
                if candidate in self.wordSet:
                    yield candidate
