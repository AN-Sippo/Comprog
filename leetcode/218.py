import heapq
from collections import defaultdict as dd


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        l = []
        for b in buildings:
            l.append((b[2], b[0], 1))
            l.append((b[2], b[1], 0))
        l.sort(key=lambda x: x[1])
        ans = []
        heap = []
        freq_map = dd(int)

        def getMaxExists():
            if len(heap) == 0:
                return 0
            while freq_map[-heap[0]] <= 0:
                heapq.heappop(heap)
                if not heap:
                    return 0
            return -heap[0]

        N = len(l)

        def getCorSafe(idx):
            if idx >= N:
                return 0
            else:
                return l[idx][1]

        i = 0
        while i < N:
            currentHeight = getMaxExists()
            while True:
                height, cor, t = l[i]
                if t == 1:
                    heapq.heappush(heap, -height)
                    freq_map[height] += 1
                elif t == 0:
                    freq_map[height] -= 1
                if getCorSafe(i) != getCorSafe(i + 1) or i >= N:
                    break
                i += 1

            nextHeight = getMaxExists()
            if currentHeight != nextHeight:
                ans.append([cor, nextHeight])
            i += 1

        return ans
