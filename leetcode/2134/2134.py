class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        search_array = nums + nums # nums.concat(nums)
        max_sum = 0
        tmp_sum = 0
        for l in range(len(nums)):
            r = l + total - 1
            if l == 0:
                tmp_sum = sum(search_array[l:r+1])
                max_sum = max(max_sum,tmp_sum)
                continue
            tmp_sum -= search_array[l - 1]
            tmp_sum += search_array[r]
            max_sum = max(max_sum,tmp_sum)
        
        
        print(total - max_sum)
        return total - max_sum

Solution().minSwaps([0,1,1,1,0,0,1,1,0])