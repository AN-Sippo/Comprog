class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        MAX_STOCK_PRICE = 1000
        # dp[i][j]:i個目を見て、今j円の株を持っている時の資産
        # dp[i][1001]:株を持っていない
        dp = [
            [-(10**10) for _ in range(MAX_STOCK_PRICE + 2)]
            for _ in range(len(prices) + 2)
        ]
        dp[0][1001] = 0
        ans = 0
        for i, price in enumerate(prices):
            # sell or pass
            for current_stock in range(MAX_STOCK_PRICE + 1):
                # sell
                dp[i + 2][1001] = max(dp[i + 2][1001], dp[i][current_stock] + price)
                ans = max(ans, dp[i + 2][1001])

                # pass
                dp[i + 1][current_stock] = max(
                    dp[i + 1][current_stock], dp[i][current_stock]
                )

            # buy
            dp[i + 1][price] = max(dp[i + 1][price], dp[i][1001] - price)

            # pass
            dp[i + 1][1001] = max(dp[i + 1][1001], dp[i][1001])

        return ans
