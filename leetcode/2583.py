import heapq
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        sums = []
        queue = deque([(root, 1)])
        current_sum = 0
        prev_depth = 1
        while queue:
            node, depth = queue.popleft()
            if depth != prev_depth:
                prev_depth = depth
                heapq.heappush(sums, -current_sum)
                current_sum = 0
            current_sum += node.val
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        heapq.heappush(sums, -current_sum)

        if len(sums) < k:
            return -1

        for _ in range(k - 1):
            heapq.heappop(sums)

        return -heapq.heappop(sums)
