class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        i = 0
        while i <= len(words) - 1:
            nowWords = [words[i]]
            nowlen = len(words[i])
            numchar = len(words[i])
            i += 1
            while i <= len(words) - 1 and nowlen + len(words[i]) + 1 <= maxWidth:
                nowWords.append(words[i])
                nowlen += len(words[i]) + 1
                numchar += len(words[i])
                i += 1
            if len(nowWords) != 1 and i != len(words):
                numblanks = maxWidth - numchar
                quotient, remainder = numblanks // (len(nowWords)-1), numblanks % (len(nowWords)-1)
                blanks = [quotient] * (len(nowWords)-1)
                for j in range(remainder):
                    blanks[j] += 1

                nowSentence = nowWords[0]
                for j in range(1, len(nowWords)):
                    nowSentence += ' ' * blanks[j-1]
                    nowSentence += nowWords[j]
                ret.append(nowSentence)
            else:
                nowSentence = nowWords[0]
                for j in range(1, len(nowWords)):
                    nowSentence += ' '
                    nowSentence += nowWords[j]
                nowSentence += ' ' * (maxWidth - nowlen)
                ret.append(nowSentence)
        return ret
