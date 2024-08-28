from math import ceil


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        M, N = len(nums1), len(nums2)
        med = ceil((M + N) / 2)

        def get1(idx):
            if idx < 0:
                return -1
            elif idx >= M:
                return 100000000
            else:
                return nums1[idx]

        def get2(idx):
            if idx < 0:
                return -1
            elif idx >= N:
                return 100000000
            else:
                return nums2[idx]

        def count(v):
            ans = 0

            ok = -1  # ok:nums2[ok]はvより小さい
            ng = N

            def solve(idx):
                if get2(idx) <= v:
                    return True
                else:
                    return False

            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if solve(mid):
                    ok = mid
                else:
                    ng = mid
            ans += ok + 1

            ok = -1  # ok:nums2[ok]はvより小さい
            ng = M

            def solve(idx):
                if get1(idx) <= v:
                    return True
                else:
                    return False

            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if solve(mid):
                    ok = mid
                else:
                    ng = mid
            ans += ok + 1

            return ans

        def solve1(idx):
            v = get1(idx)
            ok = -1  # ok:nums2[ok]はvより小さい
            ng = N

            def solve(idx):
                if get2(idx) < v:
                    return True
                else:
                    return False

            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if solve(mid):
                    ok = mid
                else:
                    ng = mid
            if idx + ok + 2 <= med:
                return True
            else:
                return False

        def solve2(idx):
            v = get2(idx)
            ok = -1  # ok:nums2[ok]はvより小さい
            ng = M

            def solve(idx):
                if get1(idx) < v:
                    return True
                else:
                    return False

            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if solve(mid):
                    ok = mid
                else:
                    ng = mid
            if idx + ok + 2 <= med:
                return True
            else:
                return False

        ok = -1  # nums[ok]は中央値以下
        ng = M  # nums[ng]は中央値より大きい

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if solve1(mid):
                ok = mid
            else:
                ng = mid

        ok1 = -1
        ng1 = N
        while abs(ok1 - ng1) > 1:
            mid = (ok1 + ng1) // 2
            if solve2(mid):
                ok1 = mid
            else:
                ng1 = mid

        ans = max(get1(ok), get2(ok1))
        if (M + N) % 2 == 1:
            return ans

        # 同じ数字が２連続である可能性
        if (
            get1(ok - 1) == ans or get2(ok1 - 1) == ans or get1(ok) == get2(ok1)
        ) and count(ans) > med:
            return ans
        else:
            return (ans + min(get1(ng), get2(ng1))) / 2
