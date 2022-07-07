class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        N = len(s)
        isPalindromic = [[False] * N for _ in range(N)]
        
        # case1: all single character
        for i in range(N):
            isPalindromic[i][i] = True
        ret += N
        
        # case2: all double characters
        for i in range(N-1):
            if s[i] == s[i+1]:
                isPalindromic[i][i+1] = True
                ret += 1
        
        # case3: rest
        for length in range(3, N+1):
            for i in range(N-length+1):
                if isPalindromic[i+1][i+length-2] and s[i] == s[i+length-1]:
                    isPalindromic[i][i+length-1] = True
                    ret += 1
        
        return ret
