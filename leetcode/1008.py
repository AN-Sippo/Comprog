# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]):
        def insert(root, node):
            current = root
            val = node.val
            while True:
                if current.val > val:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right

        root = TreeNode(val=preorder[0])
        for val in preorder[1:]:
            insert(root, TreeNode(val=val))
        return root
