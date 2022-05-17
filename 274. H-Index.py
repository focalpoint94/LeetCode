class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ret = 0
        for i, citation in enumerate(citations, 1):
            if citation >= i:
                ret = max(ret, i)
            else:
                break
        return ret
