class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """

        #init union find
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]


        def find(x):
            if par[x] == x:
                return x
            else:
                par[x] = find(par[x])
                return par[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            if par[x] == par[y]:
                return 
            if rank[x] > rank[y]:
                x,y = x,y 
            par[x] = y 
            if rank[x] == rank[y]:
                rank[y] += 1
        
        def same(x,y):
            return find(x) == find(y)
        
        logs.sort(key=lambda x:x[0])
        ans = 0
        for log in logs:
            timestamp,xi,yi = log 
            if same(xi,yi):
                continue 
            union(xi,yi)
            ans = timestamp

        root = find(0)
        for i in range(n):
            if root != find(i):
                return -1
        return ans


print(Solution().earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]],4))