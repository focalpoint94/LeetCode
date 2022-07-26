class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        
        def dfs(opn, end, path):
            if opn == 0:
                ret.append(path + ')' * end)
                return
            if opn > end:
                return
            dfs(opn-1, end, path+'(')
            dfs(opn, end-1, path+')')
        
        dfs(n, n, '')
        return ret
