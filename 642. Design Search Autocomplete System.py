import heapq
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        for i, sentence in enumerate(sentences):
            self.insert(sentence, times[i])
        
        self.freqs = {sentences[i]: times[i] for i in range(len(sentences))}
        self.buffer = ''
        self.node = self.trie
        self.noneAvailable = False
    
    
    def insert(self, sentence, time):
        t = self.trie
        for c in sentence:
            if c not in t:
                t[c] = {}
            t = t[c]
            # t['@']: stores matching sentences 
            if '@' not in t:
                t['@'] = []
            heapq.heappush(t['@'], (-time, sentence))
        # end symbol
        t['#'] = '#'

        
    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.buffer in self.freqs:
                self.freqs[self.buffer] += 1
            else:
                self.freqs[self.buffer] = 1
            self.insert(self.buffer, self.freqs[self.buffer])
            self.buffer = ''
            self.node = self.trie
            self.noneAvailable = False
            return []
        
        self.buffer += c
        
        if self.noneAvailable or c not in self.node:
            self.noneAvailable = True
            return []
        
        self.node = self.node[c]
        ret = []
        tobePushed = []
        while len(ret) < 3:
            if not self.node['@']:
                break
            time, sentence = heapq.heappop(self.node['@'])
            if sentence not in ret:
                ret.append(sentence)
                tobePushed.append((time, sentence))
        for i in range(len(tobePushed)):
            heapq.heappush(self.node['@'], tobePushed[i])
        return ret

            


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
