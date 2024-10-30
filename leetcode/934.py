from sys import setrecursionlimit
from collections import deque

setrecursionlimit(1000000)


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)

        visited = [[False for _ in range(n)] for _ in range(n)]
        queue = deque()

        def dfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = True
            if grid[x][y] == 1:
                grid[x][y] = 2
                queue.append((x, y, 0))
                for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                        continue
                    dfs(next_x, next_y)

        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        visited = [[False for _ in range(n)] for _ in range(n)]
        while queue:
            x, y, dist = queue.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            if grid[x][y] == 1:
                return dist - 1
            for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                    continue
                queue.append((next_x, next_y, dist + 1))
