import random


class Solution:

    def __init__(self, w: list[int]):
        n = len(w)
        self.tot = sum(w)
        self.sums = [0 for _ in range(n)]
        self.sums[0] = w[0]
        for i in range(1, n):
            self.sums[i] = self.sums[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = random.random() * self.tot

        def solve(mid, target):
            return self.sums[mid] >= target

        ok = len(self.sums)
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid, target):
                ok = mid
            else:
                ng = mid

        return ok


s = Solution([1])
s.pickIndex()
