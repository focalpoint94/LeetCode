INF = int(1e9)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = {}
        if self.dfs(coins, amount) == INF:
            return -1
        return self.dfs(coins, amount)
        
    def dfs(self, coins, amount):
        if amount == 0:
            return 0
        if amount in self.dp:
            return self.dp[amount]
        ret = INF
        for coin in coins:
            if amount - coin >= 0:
                ret = min(ret, self.dfs(coins, amount-coin) + 1)
        self.dp[amount] = ret
        return ret
