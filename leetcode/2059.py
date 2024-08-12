import collections


class Solution:
    def minimumOperations(self, nums, start, goal):
        visited = [0 for _ in range(1001)]
        queue = collections.deque()
        for n in nums:
            if self.isValid(goal + n):
                queue.append((goal + n, 1))
            if self.isValid(goal - n):
                queue.append((goal - n, 1))
            if self.isValid(goal ^ n):
                queue.append((goal ^ n, 1))

        while queue:
            val, cnt = queue.popleft()
            if visited[val]:
                continue
            if val == start:
                return cnt

            visited[val] = 1
            for n in nums:
                plus = val + n
                if self.isValid(plus):
                    queue.append((plus, cnt + 1))
                minus = val - n
                if self.isValid(minus):
                    queue.append((minus, cnt + 1))
                xor = val ^ n
                if self.isValid(xor):
                    queue.append((xor, cnt + 1))

        return -1

    def isValid(self, num):
        return 0 <= num <= 1000


print(Solution().minimumOperations([2, 4, 12], 2, 12))
