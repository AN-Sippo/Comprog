from math import ceil


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        ans = 0
        s = "".join(map(str, seats))
        l = s.split("1")
        if seats[0] != 1:
            ans = max(ans, len(l[0]))
        if seats[-1] != 1:
            ans = max(ans, len(l[-1]))

        for si in l:
            ans = max(ans, ceil(len(si) / 2))

        return ans
