class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for idx,n in enumerate(nums):
            if n in dic:
                return [idx,dic[n]]
            else:
                dic[target - n] = idx


print(Solution().twoSum([3,2,4],6))