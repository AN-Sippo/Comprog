from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root, to_delete):
        delete_set = set(to_delete)
        queue = deque()
        queue.append(root)
        ans = []
        if root.val not in delete_set:
            ans.append(root)

        while queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
                if node.left.val in delete_set:
                    node.left = None
                elif node.val in delete_set:
                    ans.append(node.left)

            if node.right is not None:
                queue.append(node.right)
                if node.right.val in delete_set:
                    node.right = None
                elif node.val in delete_set:
                    ans.append(node.right)

        return ans
