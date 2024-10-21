class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n = len(dist)
        minutes = [0 for _ in range(n)]
        for i in range(n):
            minutes[i] = dist[i] / speed[i]
        minutes.sort()

        ans = 0
        for i, v in enumerate(minutes):
            if i < v:
                ans += 1
                continue
            return ans

        return ans
