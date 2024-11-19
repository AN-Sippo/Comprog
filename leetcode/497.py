from random import randint


class Solution:

    def __init__(self, rects: list[list[int]]):
        squares = []
        for ai, bi, xi, yi in rects:
            squares.append((abs(xi - ai) + 1) * (abs(yi - bi) + 1))
        self.selector = RandomSelect(squares)
        self.rects = rects

    def pick(self) -> list[int]:
        idx = self.selector.select()
        ai, bi, xi, yi = self.rects[idx]
        ans = [randint(ai, xi), randint(bi, yi)]
        return ans

    def check(self, point):
        xx, yy = point
        return any([ai <= xx <= xi and bi <= yy <= yi for ai, bi, xi, yi in self.rects])


class RandomSelect:
    def __init__(self, weights: list[int]):
        self.n = len(weights)
        for i in range(1, self.n):
            weights[i] += weights[i - 1]
        self.sums = weights
        self.max = weights[-1]

    def select(self):
        val = randint(1, self.max)
        idx = self.binary_search(val)
        return idx

    def binary_search(self, val):
        if self.sums[0] >= val:
            return 0

        def solve(mid):
            return self.sums[mid] >= val

        ok = self.n - 1
        ng = 0
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
