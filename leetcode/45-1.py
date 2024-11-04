from collections import deque


class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])

        current_farthest = 0
        while queue:
            current, depth = queue.popleft()
            if current == n - 1:
                return depth

            for next in range(
                max(current_farthest + 1, current + 1),
                min(current + nums[current] + 1, n),
            ):
                queue.append((next, depth + 1))
            current_farthest = max(current_farthest, next)
