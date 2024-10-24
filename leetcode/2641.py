# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def replaceValueInTree(self, root):
        sums = {}
        queue = deque([root])
        root.val = 0
        depth = 0
        while queue:
            size = len(queue)
            current_sum = 0
            for _ in range(size):
                node = queue.popleft()
                current_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            sums[depth] = current_sum
            depth += 1

        queue = deque([root])
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left and node.right:
                    this_sum = node.left.val + node.right.val
                    node.left.val = sums[depth] - this_sum
                    node.right.val = sums[depth] - this_sum
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left:
                    node.left.val = sums[depth] - node.left.val
                    queue.append(node.left)
                elif node.right:
                    node.right.val = sums[depth] - node.right.val
                    queue.append(node.right)

        return root
