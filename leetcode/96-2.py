class Solution:
    def numTrees(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]

        def count(l: int) -> int:
            if memo[l] != -1:
                return memo[l]

            if l == 0:
                return 1

            res = 0
            for i in range(l):
                res += count(i) * count(l - 1 - i)
            memo[l] = res
            return res

        return count(n)
