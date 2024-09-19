class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        dic = {}
        day = 0
        for v in tasks:
            day += 1
            if v in dic:
                post_days = day - dic[v]
                break_days = max(0, space - post_days + 1)
                day += break_days
            dic[v] = day

        return day
