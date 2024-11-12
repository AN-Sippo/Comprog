class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        self.n = len(items)
        items.sort()
        costs = [v for v, b in items]
        beauties = [b for v, b in items]
        self.costs = costs
        for i in range(1, self.n):
            beauties[i] = max(beauties[i - 1], beauties[i])
        ans = []

        def solve(query):
            idx = self.binary_search(query)
            if idx == -1:
                return 0
            return beauties[idx]

        for query in queries:
            ans.append(solve(query))
        return ans

    def binary_search(self, value):
        if self.costs[0] > value:
            return -1
        # value以下の価格の最大値であるインデックスを求める
        n = self.n
        ok = 0
        ng = n
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if self.binary_search_solve(mid, value):
                ok = mid
            else:
                ng = mid
        return ok

    def binary_search_solve(self, idx, price):
        if self.costs[idx] > price:
            return False
        else:
            return True
