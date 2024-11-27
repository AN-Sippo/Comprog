from collections import defaultdict as dd
from heapq import heappush, heappop


class Solver:
    def __init__(self, arr: list[int], k: int):
        assert len(arr) == k
        self.freq_map = dd(int)
        self.before = arr[-1]
        asc_cnt = 0
        before = 0
        self.heap = []
        for v in arr:
            heappush(self.heap, -v)
            self.freq_map[v] += 1
            if before == v - 1:
                asc_cnt += 1
            else:
                asc_cnt = 1
            before = v

        self.asc_cnt = asc_cnt
        self.k = k

    def ascending(self) -> bool:
        return self.asc_cnt >= self.k

    def append_pop(self, add_val, pop_val):
        if self.before == add_val - 1:
            self.asc_cnt += 1
        else:
            self.asc_cnt = 1
        self.before = add_val
        self.freq_map[add_val] += 1
        self.freq_map[pop_val] -= 1
        heappush(self.heap, -add_val)

    def max(self):
        res = -self.heap[0]
        while self.freq_map[res] <= 0:
            heappop(self.heap)
            res = -self.heap[0]
        return res


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        solver = Solver(nums[:k], k)
        ans = []
        ans.append(solver.max() if solver.ascending() else -1)

        for i in range(k, n):
            solver.append_pop(nums[i], nums[i - k])
            ans.append(solver.max() if solver.ascending() else -1)

        return ans
