class Solution:
    def racecar(self, target: int) -> int:
        self.dp = {}
        return self.helper(target)

    def helper(self, target):
        if target in self.dp:
            return self.dp[target]

        k = 1
        while 2 ** k - 1 < target:
            k += 1

        if target == 2 ** k - 1:
            self.dp[target] = k
            return k

        if target == 2 ** (k - 1) - 1:
            self.dp[target] = k - 1
            return k - 1
        
        ret = self.helper(2 ** k - 1 - target) + k + 1
        
        for m in range(k - 1):
            ret = min(ret, self.helper(target - 2 ** (k - 1) + 2 ** m) + k + m + 1)

        self.dp[target] = ret
        return ret
