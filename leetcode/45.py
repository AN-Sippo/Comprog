from collections import deque


class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])
        visited = [False for _ in range(n)]
        visited[0] = True
        while queue:
            current, depth = queue.popleft()
            if nums[current] == nums[-1]:
                return depth
            for next in range(current + 1, min(n, current + nums[current] + 1)):
                if visited[next]:
                    continue
                visited[next] = True
                queue.append((next, depth + 1))
