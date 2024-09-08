class SegmentTree:
    def __init__(self, n, initial, default_value, compare):
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
        while k > 0:
            k = (k - 1) // 2
            self.tree[k] = self.compare(self.tree[k * 2 + 1], self.tree[k * 2 + 2])

    def left_child(self, k):
        return 2 * k + 1

    def right_child(self, k):
        return 2 * k + 2

    def query(self, a, b):
        # 区間(a,b]
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


h, w, q = map(int, input().split())
remained = [[True for _ in range(w)] for _ in range(h)]

rows_min = [SegmentTree(w, range(w), w, min) for _ in range(h)]
rows_max = [SegmentTree(w, range(w), -1, max) for _ in range(h)]
cols_min = [SegmentTree(h, range(h), h, min) for _ in range(w)]
cols_max = [SegmentTree(h, range(h), -1, max) for _ in range(w)]


def explode(ri, ci):
    if 0 <= ri < h and 0 <= ci < w:
        # そこに壁があることを前提。
        remained[ri][ci] = False
        rows_min[ri].update(ci, w)
        rows_max[ri].update(ci, -1)
        cols_min[ci].update(ri, h)
        cols_max[ci].update(ri, -1)


for _ in range(q):
    ri, ci = map(lambda x: int(x) - 1, input().split())
    if remained[ri][ci]:
        explode(ri, ci)
        continue

    if ci > 0:
        ci_l = rows_max[ri].query(0, ci)
        explode(ri, ci_l)
    if ci < w - 1:
        ci_r = rows_min[ri].query(ci + 1, w)
        explode(ri, ci_r)
    if ri > 0:
        ri_t = cols_max[ci].query(0, ri)
        explode(ri_t, ci)
    if ri < h - 1:
        ri_b = cols_min[ci].query(ri + 1, h)
        explode(ri_b, ci)


print(sum([sum(i) for i in remained]))
