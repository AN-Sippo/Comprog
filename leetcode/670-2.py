class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        N = len(num)
        max_idx = N - 1
        a = b = 0
        for i, current in zip(range(N)[::-1], reversed(num)):
            _max = num[max_idx]
            if _max > current:
                a = i
                b = max_idx
            elif _max < current:
                max_idx = i
        num[a], num[b] = num[b], num[a]
        return int("".join(num))
