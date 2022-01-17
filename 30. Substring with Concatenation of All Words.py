class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        ret = []
        wordSet = set(words)
        n, m = len(words), len(words[0])
        for i in range(m):
            wordCounter = Counter(words)
            k = j = i
            while j + m <= len(s):
                if j - k >= n * m:
                    if s[k:k+m] in wordSet:
                        wordCounter[s[k:k+m]] += 1
                    k += m
                word = s[j:j+m]
                if word in wordSet:
                    wordCounter[word] -= 1
                j += m
                if self.is_Finish(wordSet, wordCounter):
                    ret.append(j - n * m)
        return ret
    
    def is_Finish(self, wordSet, wordCounter):
        for word in wordSet:
            if wordCounter[word] != 0:
                return False
        return True
