class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        sum_l = [0]  # sum_l[i]:(0:i]の累積和
        for i in range(n):
            sum_l.append(sum_l[-1] + nums[i])

        ans = -(10**10)
        _min = 0
        for i in range(n):
            sum_v = sum_l[i + 1]
            ans = max(ans, sum_v - _min)
            _min = min(_min, sum_v)

        return ans
