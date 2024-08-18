class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        s = set()
        for xi, yi in points:
            s.add((xi, yi))

        ans = 10**10
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in s and (x2, y1) in s:
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        if ans == 10**10:
            return 0
        return ans
