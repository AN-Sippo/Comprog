from math import sqrt


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for xi, yi in points:
            distances.append(xi**2 + yi**2)

        def split(remaining: list[int], mid: int):
            closer, father = [], []
            for idx in remaining:
                if distances[idx] <= mid:
                    closer.append(idx)
                else:
                    father.append(idx)
            return closer, father

        n = len(points)
        remaining = [i for i in range(n)]

        ans = []
        ok = 0
        ng = max(distances) + 1
        while k:
            mid = (ok + ng) // 2
            closer, father = split(remaining, mid)
            if len(closer) <= k:
                ans.extend(closer)
                k -= len(closer)
                remaining = father
                ok = mid
            else:
                remaining = closer
                ng = mid

        return [points[i] for i in ans]


Solution().kClosest([[1, 3], [-2, 2]], 1)
