class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = []
        last = {c: i for i, c in enumerate(s)}
        start = boundary = 0
        for i, c in enumerate(s):
            boundary = max(boundary, last[c])
            if boundary == i:
                ret.append(boundary-start+1)
                start = i + 1
        return ret
