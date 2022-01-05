class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = []
        self.helper(n, n, '')
        return self.ret
    
    def helper(self, l, r, path):
        if l == 0:
            self.ret.append(path + (')' * r))
            return
        if l == r:
            self.helper(l-1, r, path + '(')
        else:
            self.helper(l-1, r, path + '(')
            self.helper(l, r-1, path + ')')
    
