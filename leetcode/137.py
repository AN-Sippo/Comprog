from collections import defaultdict as dd


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = set()
        freq_map = dd(int)
        for n in nums:
            ans.add(n)
            freq_map[n] += 1
            if freq_map[n] == 3:
                ans.remove(n)

        return ans.pop()
