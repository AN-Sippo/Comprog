import math

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        coDetenateMap = {}
        for idx,bomb in enumerate(bombs):# O(n^2)
            coDetenateMap[idx] = []
            for targetIdx,targetBomb in enumerate(bombs): 
                if targetIdx == idx:
                    continue 
                if self.coDetonate(bomb,targetBomb):
                    coDetenateMap[idx].append(targetIdx)
        
        maxCoDetonate = 0
        for idx,bomb in enumerate(bombs): #O(N+E) : E <= n^2
            currentCoDetonateSum = 0
            Detonated = [False for _ in range(len(bombs))]
            queue = [idx]
            queue.extend(coDetenateMap[idx])

            while queue:
                nextIdx = queue.pop()
                if Detonated[nextIdx]:
                    continue

                currentCoDetonateSum += 1
                Detonated[nextIdx] = True
                for  j in coDetenateMap[nextIdx]:
                    if  Detonated[j]:
                        continue
                    queue.append(j)
            
            maxCoDetonate = max(maxCoDetonate,currentCoDetonateSum)
        
        print(maxCoDetonate)
        return maxCoDetonate
                        
    
    def coDetonate(self,first,second):
        return  math.sqrt(pow(first[0] - second[0],2)  + pow(first[1] - second[1],2)) <= first[2]


Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])