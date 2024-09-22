from collections import defaultdict as dd


class FrequencyMap:
    def __init__(self, nums):
        self.nums = nums
        self.dic = dd(int)
        self.left_idx = 0
        self.length = 0

    def pop(self):
        self.dic[self.nums[self.left_idx]] -= 1
        self.left_idx += 1
        self.length -= 1

    def add(self, key):
        self.dic[key] += 1
        self.length += 1

    def get(self, key):
        return self.dic[key]


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        ans = 0
        fqm = FrequencyMap(nums)
        for n in nums:
            fqm.add(n)
            while fqm.get(n) > k:
                fqm.pop()
            ans = max(ans, fqm.length)

        return ans
