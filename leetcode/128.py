class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        before = 10**10
        ans  = 0
        tmp = 0
        for i in nums:
            if i == before + 1 :
                tmp += 1
            elif i == before:
                pass
            else:
                tmp = 1
            ans = max(ans,tmp)  
            before = i
        return ans 

                
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))