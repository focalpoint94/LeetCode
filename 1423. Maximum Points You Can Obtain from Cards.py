class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        prefixSum = [0]
        for point in cardPoints:
            prefixSum.append(prefixSum[-1] + point)
        
        ret = -1
        for i in range(0, k+1):
            j = k - i
            ret = max(ret, prefixSum[i]-prefixSum[0]+prefixSum[N]-prefixSum[N-j])
        return ret
