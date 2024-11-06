from sys import setrecursionlimit

setrecursionlimit(10**6)


class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {1: 0}

        def search(current: int):
            if current in memo:
                return memo[current]
            if current % 2 == 0:
                ans = search(current // 2) + 1
                memo[current] = ans
                return ans
            else:
                ans = min(search(current - 1), search(current + 1)) + 1
                memo[current] = ans
                return ans

        return search(n)
