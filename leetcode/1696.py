class SegmentTree:
    def __init__(self, n) -> None:
        min_int = -(10**10)
        l = 1
        self.default = min_int
        while l < n:
            l *= 2
        self.length = l * 2 - 1
        self.n = l
        self.tree = [min_int for _ in range(self.length)]

    def getIndex(self, i: int) -> int:
        return i + self.n - 1

    def update(self, x: int, v: int) -> None:
        # x番目の要素をvにする
        k = self.getIndex(x)
        self.tree[k] = v
        while k > 0:
            k = (k - 1) // 2
            left = self.tree[k * 2 + 1]
            right = self.tree[k * 2 + 2]
            self.tree[k] = max(left, right)

    def query(self, a: int, b: int) -> int:
        a = max(a, 0)
        b = min(b, self.n)

        # 区間[a,b)での最大値を求める
        # k:今から探索するノード
        # l:今から探索するノードが担当している区間[l,r)
        def q(a: int, b: int, k: int, l: int, r: int):
            if k >= self.length:
                return self.default
            left_idx = k * 2 + 1
            right_idx = k * 2 + 2
            if a >= r or b <= l:
                return self.default
            elif a <= l and b >= r:
                return self.tree[k]
            else:
                right = q(a, b, right_idx, (r + l) // 2, r)
                left = q(a, b, left_idx, l, (r + l) // 2)
                return max(left, right)

        return q(a, b, 0, 0, self.n)


class Solution:
    def maxResult(self, nums, k):
        N = len(nums)
        tree = SegmentTree(N)
        tree.update(0, nums[0])
        for i in range(1, N):
            before = tree.query(max(i - k, 0), i)
            n = nums[i]
            tree.update(i, n + before)

        return tree.query(N - 1, N)


print(Solution().maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))


class SegmentTree:
    def __init__(self, n):
        self.default_value = -(10**10)  # 最大値を求める場合はめっちゃ小さく。
        l = 1
        while l < n:
            l *= 2
        self.N = l
        self.length = 2 * self.N - 1
        self.tree = [self.default_value for _ in range(self.length)]

    def getIndex(self, k):
        return k + self.N - 1

    def update(self, i, v):
        k = self.getIndex(i)
        self.tree[k] = v
        # 祖先ノードも更新する
        while k > 0:  # ここを「k >= 0」で条件づけるとk = 0でループに入りバグる。
            k = (k - 1) // 2
            left = self.tree[k * 2 + 1]
            right = self.tree[k * 2 + 2]
            self.tree[k] = max(left, right)

    def query(self, a, b):
        # 区間[a,b)における最大値を求める。（元の配列で言うところの）
        # k:今見ているノードのインデックス
        # k:今見ているノードが元の配列の区間[l,r)に対応している。
        def q(a, b, k, l, r):
            if k >= self.length:
                return self.default_value
            if a >= r or b <= l:
                return self.default_value
            elif l >= a and r <= b:
                return self.tree[k]
            else:
                left = q(a, b, k * 2 + 1, l, (l + r) // 2)
                right = q(a, b, k * 2 + 2, (l + r) // 2, r)
                return max(left, right)

        return q(a, b, 0, 0, self.N)
