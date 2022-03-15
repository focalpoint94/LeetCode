class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # [index, source, target]
        matched = []
        k = len(indices)
        for i in range(k):
            idx, source, target = indices[i], sources[i], targets[i]
            # match?
            if s[idx:idx+len(source)] == source:
                matched.append((idx, source, target))
        
        matched.sort()
        strList, prv = [], 0
        for idx, source, target in matched:
            strList.append(s[prv:idx])
            strList.append(target)
            prv = idx + len(source)
        strList.append(s[prv:])
        
        return ''.join(strList)
