from math import sqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        big = []

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                small.append(i)
                big.append(n // i)

        if small[-1] == big[-1]:
            big.pop()

        factors = small + big[::-1]
        if len(factors) < k:
            return -1

        return factors[k - 1]
