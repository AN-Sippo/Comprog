class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        INF = 10**5

        def check(x):
            top_cnt = 0
            bottom_cnt = 0
            for top, bottom in zip(tops, bottoms):
                if top == x and bottom == x:
                    pass
                elif top == x:
                    bottom_cnt += 1
                elif bottom == x:
                    top_cnt += 1
                else:
                    return -1
            return min(top_cnt, bottom_cnt)

        a = tops[0]
        b = bottoms[0]

        a_cnt = check(a)
        b_cnt = check(b)
        if a_cnt == b_cnt == -1:
            return -1
        elif a_cnt == -1:
            return b_cnt
        elif b_cnt == -1:
            return a_cnt
        else:
            return min(a_cnt, b_cnt)
