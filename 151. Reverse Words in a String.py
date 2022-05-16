class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        nwords = []
        for word in words[::-1]:
            if word:
                nwords.append(word)
        return ' '.join(nwords)
