class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
            return 0
        ret = 0
        q = [[beginWord, 1]]
        while q:
            next_q = []
            for elem in q:
                prev, length = elem
                tobe_removed = set()
                for neighbor in get_neighbors(prev):
                    if neighbor == endWord:
                        return length + 1
                    else:
                        next_q.append([neighbor, length+1])
                        tobe_removed.add(neighbor)
                wordSet -= tobe_removed
            q = next_q
        return 0
