from collections import defaultdict as dd


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        dic = {}
        for i in range(ord("a"), ord("z") + 1):
            dic[chr(i)] = dd(int)

        def get(i):
            if i >= n:
                return ""
            else:
                return s[i]

        ans = 0
        idx = 0
        while idx < n:
            si = get(idx)
            length = 1
            idx_diff = 1
            while get(idx + idx_diff) == si:
                length += 1
                idx_diff += 1
            ans = max(ans, length - 2)
            dic[si][length - 1] += 2
            if dic[si][length - 1] >= 3:
                ans = max(ans, length - 1)

            dic[si][length] += 1
            if dic[si][length] == 3:
                ans = max(ans, length)
            idx += idx_diff

        return ans if ans else -1
