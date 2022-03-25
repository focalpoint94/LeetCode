from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for char in word[::-1]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = '#'
        self.q = deque(maxlen=2000)

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        node = self.trie
        for i in range(len(self.q)-1, -1, -1):
            letter = self.q[i]
            if letter not in node:
                return False
            node = node[letter]
            if '#' in node:
                return True
        return False
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
