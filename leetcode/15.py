class Solution:
    def threeSum(self, nums):
        d = {}
        ans = []
        nums.sort()
        i = 0
        while i < len(nums):
            if i != 0:
                while nums[i] == nums[i - 1]:
                    i+= 1
                    if i == len(nums):
                        return ans
            
            m = i + 1
            r = len(nums) - 1
            while r > m:
                sum = nums[i] + nums[m] + nums[r]
                if sum == 0:
                    ans.append([nums[i],nums[m],nums[r]])
                    m += 1
                    if m == r:
                        break
                    while nums[m] == nums[m-1]:
                        if m == r:
                            break
                        m += 1
                elif sum < 0:
                    m += 1

                else:
                    r -=1 
            i += 1
        return ans
                    

    

print(Solution().threeSum([0,0,0]))