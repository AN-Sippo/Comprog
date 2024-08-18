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

        def solve(node: TreeNode, l: TreeNode, r: TreeNode, ans: list[TreeNode]) -> int:
            # 処理を続けるなら0.continueなら1.breakなら2を返す。
            # ansは参照を受けて更新していくか、値を返す。
            if l is not None:
                if node.val in delete_set and l.val not in delete_set:
                    ans.append(l)
                elif l.val in delete_set:
                    node.left = None
            if r is not None:
                if node.val in delete_set and r.val not in delete_set:
                    ans.append(r)
                elif r.val in delete_set:
                    node.right = None
            return 0

        while queue:
            # ここで取り出したnodeに対して、node.leftとnode.rightそれぞれ確認していく。
            # Noneが取り出されることはないことを保証する。
            node = queue.pop()
            l = node.left
            r = node.right
            res = solve(node, l, r, ans)
            if res == 2:
                break
            elif res == 1:
                continue
            elif res == 0:
                if l is not None:
                    queue.append(l)
                if r is not None:
                    queue.append(r)

        return ans
