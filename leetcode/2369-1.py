class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        N = len(nums)
        # dp[i]：(:i]がokであるか。
        dp = [False for _ in range(N + 1)]
        dp[0] = True
        dp[1] = False
        for i in range(1, N):
            j = i + 1
            if nums[i] == nums[i - 1]:
                dp[j] = dp[j] | dp[j - 2]

            if i == 1:
                continue

            if nums[i] == nums[i - 1] == nums[i - 2]:
                dp[j] = dp[j] | dp[j - 3]
            if nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                dp[j] = dp[j] | dp[j - 3]

        return dp[N]
