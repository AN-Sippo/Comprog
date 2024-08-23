class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # dp[i]:区間(:i)における、iを終端としたarithmeticなsubarrayの数
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2, N):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)
