class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        edges = [[] for _ in range(n)]
        for start in range(n):
            for end in range(n):
                if end == start:
                    continue
                if isConnected[start][end]:
                    edges[start].append(end)

        visited = [False for _ in range(n)]
        ans = 0

        def dfs(current):
            if visited[current]:
                return
            visited[current] = True
            for next in edges[current]:
                if visited[next]:
                    continue
                dfs(next)

        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans
