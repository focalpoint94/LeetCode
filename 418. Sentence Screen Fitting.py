class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        self.sentence = [len(word) for word in sentence]
        self.cols = cols
        self.dp = {}
        total, idx = 0, 0
        for i in range(rows):
            cnt, idx = self.calc(idx)
            total += cnt
        return total
    
    def calc(self, idx):
        if idx in self.dp:
            return self.dp[idx]
        cnt = 0 
        summed, i = 0, idx
        while summed + self.sentence[i] <= self.cols:
            summed += self.sentence[i] + 1
            i += 1
            if i == len(self.sentence):
                cnt += 1
                i = 0
        self.dp[idx] = cnt, i
        return cnt, i
