class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def get_neighbors(word):
            neighbors = []
            alphas = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(len(word)):
                for j in range(len(alphas)):
                    candidate = word[:i] + alphas[j] + word[i+1:]
                    if candidate in wordSet:
                        neighbors.append(candidate)
            return neighbors
        
        wordSet = set(wordList)
        wordSet.discard(beginWord)
        if endWord not in wordSet:
            return []
        ret = []
        q, finish = [[beginWord]], False
        while q and not finish:
            next_q = []
            tobe_removed = set()
            for elem in q:
                prev = elem[-1]
                for neighbor in get_neighbors(prev):
                    if neighbor == endWord:
                        ret.append(elem+[endWord])
                        finish = True
                    else:
                        next_q.append(elem+[neighbor])
                        tobe_removed.add(neighbor)
            wordSet -= tobe_removed
            q = next_q
        return ret
