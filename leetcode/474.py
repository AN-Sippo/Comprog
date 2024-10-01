class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for str_i in strs:
            count_zero, count_one = self.count(str_i)
            for current_zero in range(m - count_zero, -1, -1):
                for current_one in range(n - count_one, -1, -1):
                    zero_idx = current_zero + count_zero
                    one_idx = current_one + count_one
                    dp[zero_idx][one_idx] = max(
                        dp[current_zero][current_one] + 1,
                        dp[zero_idx][one_idx],
                    )

        return dp[m][n]

    def count(self, binary_string: str) -> list[int]:
        count_zero = 0
        count_one = 0
        for str_i in binary_string:
            if str_i == "0":
                count_zero += 1
            elif str_i == "1":
                count_one += 1

        return [count_zero, count_one]


Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
