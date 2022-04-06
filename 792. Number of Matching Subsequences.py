from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        reg = defaultdict(list)
        for word in words:
            reg[word[0]].append(word)
        
        ret = 0
        for c in s:
            updated = []
            for word in reg[c]:
                if len(word) == 1:
                    ret += 1
                else:
                    if word[1] == c:
                        updated.append(word[1:])
                    else:
                        reg[word[1]].append(word[1:])                    
            reg[c] = updated
        return ret
