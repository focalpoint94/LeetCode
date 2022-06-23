class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ret = float('inf')
        prevWord, prevIdx = None, None
        for idx, word in enumerate(wordsDict):
            if prevWord is None and (word == word1 or word == word2):
                prevWord, prevIdx = word, idx
            elif prevWord == word1:
                if word == word1:
                    prevWord, prevIdx = word, idx
                elif word == word2:
                    ret = min(ret, idx-prevIdx)
                    prevWord, prevIdx = word, idx
            elif prevWord == word2:
                if word == word1:
                    ret = min(ret, idx-prevIdx)
                    prevWord, prevIdx = word, idx
                elif word == word2:
                    prevWord, prevIdx = word, idx
        return ret
