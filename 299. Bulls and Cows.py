class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        c1 = Counter(secret)
        c2 = Counter(guess)
        cows = 0
        for k, v in c2.items():
            cows += min(v, c1[k])
        bulls = 0
        for i, c in enumerate(secret):
            if guess[i] == c:
                bulls += 1
        cows -= bulls
        return str(bulls) + 'A' + str(cows) + 'B'
