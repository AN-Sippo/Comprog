class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        nums_ascending = sorted([(j, i) for i, j in enumerate(nums)])
        min_idx = 10**5
        ans = 0
        for value, idx in nums_ascending:
            if min_idx < idx:
                ans = max(ans, idx - min_idx)
            else:
                min_idx = idx

        return ans
