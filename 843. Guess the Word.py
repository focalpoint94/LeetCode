# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        import random
        curlist = wordlist
        for i in range(10):
            rand_idx = random.randint(0, len(curlist)-1)
            rand_word = curlist[rand_idx]
            k = master.guess(rand_word)
            if k == 6:
                return
            nextlist = []
            for word in curlist:
                num_match = 0
                for i, c in enumerate(word):
                    if rand_word[i] == c:
                        num_match += 1
                if num_match == k:
                    nextlist.append(word)
            curlist = nextlist
