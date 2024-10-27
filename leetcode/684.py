class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, a):
        if self.par[a] == a:
            return a
        else:
            self.par[a] = self.find(self.par[a])
            return self.par[a]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.rank[a] > self.rank[b]:
            a, b = b, a
        elif self.rank[a] == self.rank[b]:
            self.rank[b] += 1

        self.par[a] = b

    def same(self, a, b) -> bool:
        a = self.find(a)
        b = self.find(b)
        return a == b


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        uf = UnionFind(n)

        for current in edges:
            ai, bi = current
            ai -= 1
            bi -= 1
            if uf.same(ai, bi):
                return current
            uf.unite(ai, bi)
