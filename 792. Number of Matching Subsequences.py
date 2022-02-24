class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        dic = defaultdict(list)
        for word in words:
            dic[word[0]].append(word)
        ret = 0
        for char in s:
            temp = copy.deepcopy(dic[char])
            dic[char] = []
            for word in temp:
                if len(word) == 1:
                    ret += 1
                else:
                    dic[word[1]].append(word[1:])
        return ret
