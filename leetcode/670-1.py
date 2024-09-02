class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        N = len(num)
        l = [-1 for _ in range(N)]  # l[i] ：(i:]における最大値の最大インデックス
        l[N - 2] = N - 1
        for i in range(N - 2, 0, -1):
            if num[i] > num[l[i]]:
                l[i - 1] = i
            else:
                l[i - 1] = l[i]

        for i in range(N):
            if num[l[i]] > num[i]:
                break

        num[i], num[l[i]] = num[l[i]], num[i]
        return int("".join(map(str, num)))
