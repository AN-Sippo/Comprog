class Solution:
    def findPeakElement(self, nums):
        N = len(nums)

        def get(idx):
            if idx == -1 or idx == N:
                return -(1 << 32)
            else:
                return nums[idx]

        def solve(idx):
            if get(idx) > get(idx - 1):
                return True
            else:
                False

        ok = -1
        ng = N
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid

        return ok
