class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * (len(s) + 1)     
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    corresponding_idx = stack.pop()
                    dp[i+1] = dp[corresponding_idx] + i - corresponding_idx + 1
        return max(dp)
