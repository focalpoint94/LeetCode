from functools import lru_cache
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ret = 0

        @lru_cache(None, None)
        def dp(idx):
            nonlocal cols
            numFitted = 0
            word, pos = sentence[idx], 0
            while pos + len(word) <= cols:
                pos += len(word) + 1
                idx += 1
                if idx == len(sentence):
                    idx = 0
                    numFitted += 1
                word = sentence[idx]
            return numFitted, idx
        
        idx = 0       
        for row in range(rows):
            numFitted, idx = dp(idx)
            ret += numFitted
        return ret
            
