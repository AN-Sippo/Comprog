class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        current_far = 0
        next_far = 0
        ans = 0
        for i in range(n - 1):
            next_far = max(next_far, i + nums[i])

            if i == current_far:
                ans += 1
                current_far = next_far
        return ans
