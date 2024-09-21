from sortedcontainers import SortedSet as sl


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


n, q = map(int, input().split())
connected = [sl([i], key=lambda x: -x) for i in range(n)]


uf = UnionFind(n)
for _ in range(q):
    _type, u, v = map(int, input().split())
    if _type == 1:
        u -= 1
        v -= 1
        # print(f"row_u:{u} raw_v:{v}")
        u = uf.find(u)
        v = uf.find(v)
        # print(f"u:{u} v:{v}")
        if u != v:
            ul = connected[u]
            vl = connected[v]
            if len(ul) > len(vl):
                ul, vl = vl, ul  # len(v)の方が大きいことを保証
            for ui in ul:
                vl.add(ui)
            uf.union(u, v)
            connected[uf.find(u)] = vl
            connected[uf.find(v)] = vl

    else:
        u -= 1
        k = v
        u = uf.find(u)
        if len(connected[u]) < k:
            print(-1)
        else:
            print(connected[u][k - 1] + 1)

    # for i in connected:
    #     print(i)
