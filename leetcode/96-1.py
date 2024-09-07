class Solution:
    def numTrees(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]

        def count(a: int, b: int) -> int:
            l = b - a
            if memo[l] != -1:
                return memo[l]

            if l == 0:
                return 1

            res = 0
            for i in range(a, b):
                res += count(a, i) * count(i + 1, b)
            memo[l] = res
            return res

        return count(1, n + 1)
