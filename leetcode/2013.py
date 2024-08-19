from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.dd = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.dd[(point[0], point[1])] += 1

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        ans = 0
        for p in self.dd:
            x2, y2 = p[0], p[1]
            if x1 == x2 and y1 == y2:
                continue
            if abs(x2 - x1) != abs(y2 - y1):
                continue
            if (x1, y2) in self.dd and (x2, y1) in self.dd:
                ans += self.dd[(x1, y2)] * self.dd[(x2, y1)] * self.dd[p]

        return ans
