class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        events = []
        # 0:first開き　2:first閉じ　1:second開き　3:second閉じ
        for first in firstList:
            events.append((first[0], 0))
            events.append((first[1], 2))
        for second in secondList:
            events.append((second[0], 1))
            events.append((second[1], 3))

        events.sort()
        ans = []
        prev = 0
        first_inside = False
        second_inside = False
        for current, event in events:
            if first_inside and second_inside:
                ans.append([prev, current])
            if event == 0:
                first_inside = True
            elif event == 2:
                first_inside = False
            elif event == 1:
                second_inside = True
            elif event == 3:
                second_inside = False
            prev = current

        return ans
