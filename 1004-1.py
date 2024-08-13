class Solution:
    def longestOnes(self, nums, k):

        def solve(val, target):
            return val >= target

        def biSearchLeft(target):
            ng = -1
            ok = N
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if solve(zero_sums[mid], target):
                    ok = mid
                else:
                    ng = mid

            return ok

        N = len(nums)

        zero_sums = [0]
        for n in nums:
            before = zero_sums[-1]
            if n == 0:
                before += 1
            zero_sums.append(before)

        ans = 0
        for r in range(N):
            l_sum = zero_sums[r + 1] - k
            l_idx = biSearchLeft(l_sum)
            ans = max(ans, r + 1 - l_idx)

        return ans


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
