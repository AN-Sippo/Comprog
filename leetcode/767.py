from collections import Counter
from heapq import heappop, heappush, heapify


class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-v, k) for k, v in Counter(s).items()]
        heapify(heap)

        ans = ["_"]
        while heap:
            cnt, char = heappop(heap)
            if char == ans[-1]:
                if not heap:
                    return ""
                cnt2, char2 = heappop(heap)
                heappush(heap, (cnt, char))
                cnt, char = cnt2, char2
            ans.append(char)
            if cnt == -1:
                continue
            heappush(heap, (cnt + 1, char))

        return "".join(ans[1:])
