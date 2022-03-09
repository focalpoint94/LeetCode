class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)

        sums = [0] * (n+1)
        cul = 0
        for idx, card in enumerate(cardPoints):
            cul += card
            sums[idx+1] = cul
        def getSum(l, r):
            return sums[l] - sums[0] + sums[-1] - sums[-1-r]
        
        ret = 0
        for l in range(k+1):
            r = k - l
            ret = max(ret, getSum(l, r))
        return ret
