class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        N = len(num)
        for i in range(N):
            swap_idx = i
            swap_v = num[i] + 1
            for j in range(i + 1, N):
                if swap_v <= num[j]:
                    swap_v = num[j]
                    swap_idx = j
            if swap_idx != i:
                break
        num[i], num[swap_idx] = num[swap_idx], num[i]
        return int("".join(map(str, num)))
