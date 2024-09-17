from heapq import heappop, heappush


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for i, point in enumerate(points):
            xi, yi = points[i]
            heappush(heap, (xi**2 + yi**2, i))

        ans = []
        for _ in range(k):
            _, idx = heappop(heap)
            ans.append(points[idx])
        return ans
