class Solution:
    def numTrees(self, n: int) -> int:
        memo = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]

        def count(start, end):
            if memo[start][end] != -1:
                return memo[start][end]

            # 区間(start,end]
            n = end - start
            if n == 0:
                return 1

            res = 0
            for i in range(start, end):
                res += count(start, i) * count(i + 1, end)

            memo[start][end] = res
            return res

        return count(1, n + 1)


print(Solution().numTrees(19))
