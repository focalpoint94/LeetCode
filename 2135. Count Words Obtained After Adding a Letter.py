from collections import defaultdict
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        wordDict = defaultdict(set)
        for word in startWords:
            wordDict[len(word)].add(''.join(sorted(word)))
        
        ret = 0
        for word in targetWords:
            word = sorted(word)
            for i in range(len(word)):
                candidate = ''.join(word[:i] + word[i+1:])
                if candidate in wordDict[len(word)-1]:
                    ret += 1
                    break
        return ret
