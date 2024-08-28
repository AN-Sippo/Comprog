class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        M, N = len(nums1), len(nums2)

        def solve(k):
            aok, ang = -1, M
            bok, bng = -1, N
            while True:
                if aok >= ang - 1:
                    return nums2[k - aok - 2]
                if bok >= bng - 1:
                    return nums1[k - bok - 2]

                ai, bi = (aok + ang) // 2, (bok + bng) // 2
                av, bv = nums1[ai], nums2[bi]

                if ai + bi <= k - 2:
                    if av >= bv:
                        bok = bi
                    else:
                        aok = ai
                else:
                    if av >= bv:
                        ang = ai
                    else:
                        bng = bi

        if (M + N) % 2 == 1:
            return solve((M + N) // 2 + 1)
        else:
            c = solve((M + N) // 2)
            d = solve((M + N) // 2 + 1)
            return (c + d) / 2


print(Solution().findMedianSortedArrays([1, 3], [2]))
