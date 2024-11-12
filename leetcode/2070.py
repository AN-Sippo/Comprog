class SegmentTree:
    def __init__(self, n, initial, default_value, compare):
        # initial:初期の配列。(treeではない)。これなしで普通にnだけで生成できる時もある。
        l = 1
        while l < n:
            l *= 2
        self.default_value = default_value
        self.n = l
        self.compare = compare
        self.length = self.n * 2 - 1
        self.tree = [self.default_value for _ in range(self.length)]
        for idx, value in enumerate(initial):
            self.update(idx, value)

    def getIndex(self, k):
        return k + self.n - 1

    def update(self, k, value):
        k = self.getIndex(k)
        self.tree[k] = value
        # 祖先ノードも更新する
        while k > 0:  # ここを「k >= 0」で条件づけるとk = 0でループに入りバグる。
            k = (k - 1) // 2
            self.tree[k] = self.compare(
                self.tree[self.left_child(k)], self.tree[self.right_child(k)]
            )

    def left_child(self, k):
        return 2 * k + 1

    def right_child(self, k):
        return 2 * k + 2

    def query(self, a, b):
        # 区間[a,b)における最大値を求める。（元の配列で言うところの）
        # k:今見ているノードのインデックス
        # k:今見ているノードが元の配列の区間[l,r)に対応している。
        def q(k, a, b, l, r):
            if k >= self.length:
                return self.default_value
            elif a >= r or b <= l:
                return self.default_value
            elif a <= l and b >= r:
                return self.tree[k]
            else:
                left = q(self.left_child(k), a, b, l, (l + r) // 2)
                right = q(self.right_child(k), a, b, (l + r) // 2, r)
                return self.compare(left, right)

        return q(0, a, b, 0, self.n)


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        self.n = len(items)
        items.sort()
        costs = [v for v, b in items]
        beauties = [b for v, b in items]
        self.costs = costs
        st = SegmentTree(self.n, beauties, 0, max)
        ans = []

        def solve(query):
            idx = self.binary_search(query)
            if idx == -1:
                return 0
            return st.query(0, idx + 1)

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
