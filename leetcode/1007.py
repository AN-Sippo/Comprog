class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        INF = 10**5
        ans = [
            [0 for _ in range(6)] for _ in range(2)
        ]  # ans[0][i]:上にiを集めるときの最小回数。ans[1][i]下にiを集める時の最小回数
        for top, bottom in zip(tops, bottoms):
            top -= 1
            bottom -= 1
            for i in range(6):
                if i == top and i == bottom:
                    continue
                elif i == top:
                    ans[1][i] += 1
                elif i == bottom:
                    ans[0][i] += 1
                else:
                    ans[1][i] += INF
                    ans[0][i] += INF

        ans = min(min(ans[0]), min(ans[1]))
        if ans >= INF:
            return -1
        else:
            return ans
