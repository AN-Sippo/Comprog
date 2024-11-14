from collections import defaultdict as dd


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        ij_dic = dd(int)
        ans = 0
        for v1 in nums1:
            for v2 in nums2:
                ij_dic[v1 + v2] += 1

        for v3 in nums3:
            for v4 in nums4:
                ans += ij_dic[-(v3 + v4)]

        return ans
