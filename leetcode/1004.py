from collections import deque


class Solution:
    def longestOnes(self, nums, k):
        queue = deque()
        ans = 0
        tmp = 0
        stock = k
        for n in nums:
            if n == 0:
                while stock <= 0:
                    if not queue:
                        break
                    v = queue.popleft()
                    if v == 0:
                        stock = min(k, stock + 1)
                        tmp -= 1
                    else:
                        tmp -= 1
                if stock > 0:
                    stock -= 1
                    tmp += 1
                    queue.append(n)
            else:
                tmp += 1
                queue.append(n)

            ans = max(tmp, ans)
        return ans


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 0))
