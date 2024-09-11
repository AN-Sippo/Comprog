class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = 10**5 + 1
        m = len(intervals)
        dp = [m for _ in range(n + 1)]  # dp[]

        def get(x):
            return dp[x + 5 * 10**4 + 1]

        def set(x, v):
            dp[x + 5 * 10**4 + 1] = v

        def map_index(v):
            return v + 10**4 + 1

        intervals.sort(key=lambda x: x[1])
        interval_idx = 0
        for idx in range(-5 * 10**4, 5 * 10**4 + 1):
            if interval_idx >= m:
                return get(idx - 1)

            set(idx, get(idx - 1))
            while interval_idx < m and intervals[interval_idx][1] == idx:
                start, end = intervals[interval_idx]
                before = get(start)
                val = min(before - 1, get(end))
                set(end, val)
                interval_idx += 1

        return dp[-1]


Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
