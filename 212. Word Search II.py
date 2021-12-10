class Solution:
    def findWords(self, board, words):
        self.trie = {}
        for word in words:
            t = self.trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = '#'
        self.ret = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                self.dfs(self.trie, board, y, x, '')
        return self.ret
    
    def dfs(self, t, board, y, x, path):
        if '#' in t:
            self.ret.append(path)
            t.pop('#')
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
            return
        char = board[y][x]
        if char in t:
            board[y][x] = '#'
            self.dfs(t[char], board, y, x+1, path+char)
            self.dfs(t[char], board, y+1, x, path+char)
            self.dfs(t[char], board, y, x-1, path+char)
            self.dfs(t[char], board, y-1, x, path+char)
            board[y][x] = char
            if not t[char]:
                t.pop(char)
