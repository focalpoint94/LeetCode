class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = '#'
        
        ret = []
        m, n = len(board), len(board[0])
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        
        def dfs(node, y, x, path):
            if '#' in node:
                ret.append(''.join(path))
                node.pop('#')
            
            if 0 <= y < m and 0 <= x < n:
                char = board[y][x]
                if not node or char not in node:
                    return
                
                board[y][x] = '@'
                for d in range(4):
                    next_y, next_x = y + dy[d], x + dx[d]
                    dfs(node[char], next_y, next_x, path+[char])
                board[y][x] = char
                if not node[char]:
                    node.pop(char)
        
        for y in range(m):
            for x in range(n):
                dfs(trie, y, x, [])
        return ret
