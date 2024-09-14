from collections import deque


class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        if k == 1:
            return list(range(1, n + 1))

        l = deque(range(1, n + 1))

        ans = []
        from_left = True
        while True:
            if len(ans) == k:
                if not from_left:
                    while l:
                        ans.append(l.popleft())
                    break
                else:
                    while l:
                        ans.append(l.pop())
                    break

            if from_left:
                ans.append(l.popleft())
                from_left = False
            else:
                ans.append(l.pop())
                from_left = True

        return ans


Solution().constructArray(3, 2)
