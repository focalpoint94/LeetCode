import functools
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        self.sentence = sentence
        self.cols = cols
        ret = 0
        startIdx = 0
        for row in range(rows):
            numTimes, startIdx = self.fit(startIdx)
            ret += numTimes
        return ret
        
    @lru_cache()
    def fit(self, startIdx):
        numTimes = 0
        occupied, idx = 0, startIdx
        word = self.sentence[idx]
        while occupied + len(word) <= self.cols:
            occupied += len(word) + 1
            idx += 1
            if idx == len(self.sentence):
                idx = 0
                numTimes += 1
            word = self.sentence[idx]
        return numTimes, idx
