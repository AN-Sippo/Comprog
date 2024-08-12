import math

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        edges = []
        for idx,bomb in enumerate(bombs):
            edges.append([])
            for targetIdx,targetBom in enumerate(bombs):
                if idx == targetIdx:
                    continue 
                if math.sqrt(pow(targetBom[0] - bomb[0],2) + pow(targetBom[1] - bomb[1],2)) <= bomb[2]:
                    edges[idx].append(targetIdx)
        


        def dfs(idx):
            _max = 0
            if denotated[idx]:
                return 0
            denotated[idx] = 1 
            _max += 1
            for edge in edges[idx]:
                if denotated[edge]:
                    continue 
                _max += dfs(edge)
            return _max

        _max = 0
        for idx in range(len(bombs)):
            denotated = [0 for _ in range(len(bombs))]
            _max = max(_max,dfs(idx))
        
        return _max




                
print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))