class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(p)
        m = len(s)
        
        # matched[i][j]: (i-1)th pattern matches (j-1)th string
        matched = [[False] * (m+1) for _ in range(n+1)]
        
        matched[0][0] = True
        for j in range(1, m+1):
            matched[0][j] = False
        
        for i in range(1, n+1):
            if p[i-1] == '*':
                matched[i][0] = matched[i-1][0]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[i-1] == '*':
                    matched[i][j] = matched[i][j-1] or matched[i-1][j]
                elif p[i-1] == '?':
                    matched[i][j] = matched[i-1][j-1]
                else:
                    matched[i][j] = matched[i-1][j-1] and p[i-1] == s[j-1]
                    
        return matched[n][m]
                    
            
