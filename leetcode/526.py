class Solution:
    def countArrangement(self, n: int) -> int:
        l = [i + 1 for i in range(n)]
        ans = 0

        def permutations(idx, visited: list[bool]):
            nonlocal ans
            if idx == n + 1:
                ans += 1
                return
            for i in range(n):
                if visited[i] or (idx % l[i] != 0 and l[i] % idx != 0):
                    continue
                visited[i] = True
                permutations(idx + 1, visited)
                visited[i] = False

        permutations(1, [False for _ in range(n)])
        return ans


print(Solution().countArrangement(6))
