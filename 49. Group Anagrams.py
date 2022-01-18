class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for char in s:
                counter[ord(char) - ord('a')] += 1
            dic[tuple(counter)].append(s)
        return [x for x in dic.values()]
