from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.maxLength = 0
        self.trie = {}
        for word in words:
            t = self.trie
            for char in word[::-1]:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = '#'
            self.maxLength = max(self.maxLength, len(word))
        self.q = deque(maxlen = self.maxLength)

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        t = self.trie
        for l in self.q:
            if '#' in t:
                return True
            if l not in t:
                return False
            t = t[l]
        return '#' in t


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
