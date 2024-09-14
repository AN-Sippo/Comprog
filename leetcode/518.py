class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i, coin in enumerate(coins):
            idx = i + 1
            tmp = 0
            while tmp <= amount:
                for before in range(0, amount - tmp + 1):
                    dp[idx][before + tmp] += dp[idx - 1][before]

                tmp += coin

        return dp[n][amount]
