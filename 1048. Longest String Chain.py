class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ret = 1
        # First, we sort words by its length
        # By this way, we only need to check the previous length (or current length - 1)
        # That is, if the length(word) is k,
        # We only need to check words that have length of k - 1.
        words.sort(key=lambda word: len(word))
        # dp[word]: max chain length until the word
        dp = {}
        for word in words:
            # if length(word) == 1, max chain length = 1
            dp[word] = 1
            if len(word) == 1:
                continue
            # Now, how do we know whether word1 (length k + 1) and word2 (length k) are connected or not?
            # I think one of the most efficient way is,
            # eliminating every character one by one in word1 and check whether it is valid
            # e.g. word1 = 'abcde'
            # then, check whether 'bcde', 'acde', 'abde', 'abce', 'abcd' are valid
            for i in range(len(word)):
                temp = word[:i] + word[i+1:]
                if temp in dp:
                    dp[word] = max(dp[word], dp[temp]+1)
                    ret = max(ret, dp[word])
        return ret
