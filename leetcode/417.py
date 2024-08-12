class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        Y = len(heights)
        X = len(heights[0])
        visited = [[0 for _ in range(X)] for _ in range(Y)]
        reachable = [[0 for _ in range(X)] for _ in range(Y)]

        def dfs(x,y):
            if visited[y][x]:
                return 
            
            visited[y][x] = 1
            reachable[y][x] += 1
            for diffX,diffY in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x + diffX
                ny = y + diffY
                if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                    continue 
                if heights[ny][nx] >= heights[y][x]:
                    dfs(nx,ny)

        #pacific 
        for x in range(X):
            dfs(x,0)
        for y in range(Y):
            dfs(0,y)
        
        visited = [[0 for _ in range(X)] for _ in range(Y)]
        #atlantic
        for x in range(X):
            dfs(x,Y - 1)
        for y in range(Y):
            dfs(X -1,y)
        
        ans = []
        for x in range(X):
            for y in range(Y):
                if reachable[y][x] == 2:
                    ans.append([y,x])
        return ans


print(Solution().pacificAtlantic(

[[1]]

))

