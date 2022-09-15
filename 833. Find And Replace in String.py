class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ret = [c for c in s]
        temp = [(indice, source, target) for (indice, source, target) in sorted(zip(indices, sources, targets), reverse=True)]
        indices = [x[0] for x in temp]
        sources = [x[1] for x in temp]
        targets = [x[2] for x in temp]
        for i, index in enumerate(indices):
            if sources[i] == s[index:index+len(sources[i])]:
                ret[index:index+len(sources[i])] = [c for c in targets[i]]
        return ''.join(ret)
