class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        def dfs(i,j):
            if (not visited[i][j]) and grid[i][j] == "1":
                visited[i][j] = 1
                for diffX,diffY in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nextX = j + diffX
                    nextY = i + diffY
                    if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                        continue 
                    if visited[nextY][nextX]:
                        continue
                    if grid[nextY][nextX] == "1":
                        dfs(nextY,nextX)
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans 
    


print(Solution().numIslands([
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"],
]))