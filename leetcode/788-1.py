class Solution:
    def rotatedDigits(self, n: int) -> int:
        nlst = list(map(int, list(str(n))))
        length = len(nlst)
        dp = [
            [[0, 0] for _ in range(2)] for _ in range(length + 1)
        ]  # dp[i][j][k]:i桁まで見て,j->1でstrict,k->1でgood
        dp[0][1][0] = 1
        for i in range(1, length + 1):
            for num in [0, 1, 8]:
                if nlst[i - 1] == num:
                    dp[i][1][1] += dp[i - 1][1][1]
                    dp[i][1][0] += dp[i - 1][1][0]
                elif nlst[i - 1] > num:
                    dp[i][0][1] += dp[i - 1][1][1]
                    dp[i][0][0] += dp[i - 1][1][0]
                dp[i][0][1] += dp[i - 1][0][1]
                dp[i][0][0] += dp[i - 1][0][0]
            for num in [2, 5, 6, 9]:
                if nlst[i - 1] == num:
                    dp[i][1][1] += dp[i - 1][1][1]
                    dp[i][1][1] += dp[i - 1][1][0]
                elif nlst[i - 1] > num:
                    dp[i][0][1] += dp[i - 1][1][1]
                    dp[i][0][1] += dp[i - 1][1][0]
                dp[i][0][1] += dp[i - 1][0][1]
                dp[i][0][1] += dp[i - 1][0][0]

        return dp[length][1][1] + dp[length][0][1]


Solution().rotatedDigits(10)
