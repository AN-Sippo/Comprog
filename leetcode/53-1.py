class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        INF = -(10**10)

        def solve(left, right):
            if left >= right:
                return INF

            if left + 1 == right:
                return nums[left]

            mid = (left + right) // 2
            left_sum = right_sum = 0
            tmp = 0
            for i in range(mid - 1, left - 1, -1):
                tmp += nums[i]
                left_sum = max(left_sum, tmp)

            tmp = 0
            for i in range(mid + 1, right):
                tmp += nums[i]
                right_sum = max(tmp, right_sum)

            return max(
                nums[mid] + left_sum + right_sum,
                solve(left, mid),
                solve(mid + 1, right),
            )

        return solve(0, len(nums))


print(Solution().maxSubArray([1]))
