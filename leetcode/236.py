class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        p_path = []
        q_path = []

        def dfs(current: TreeNode, path: list[TreeNode]):
            nonlocal p_path, q_path
            if q_path and p_path:
                return

            if current == p:
                p_path = path[:]
            elif current == q:
                q_path = path[:]

            if current.left:
                path.append(current.left)
                dfs(current.left, path)
                path.pop()

            if current.right:
                path.append(current.right)
                dfs(current.right, path)
                path.pop()

        dfs(root, [root])
        for pi in reversed(p_path):
            for qi in reversed(q_path):
                if pi == qi:
                    return pi
