# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        n = len(preorder)
        in_o_dic = {}
        for i, v in enumerate(inorder):
            in_o_dic[v] = i

        def search(pre_start, pre_end, in_start, in_end):
            # (pre_start,pre_end]
            if pre_end - pre_start <= 0:
                return
            root_val = preorder[pre_start]
            root = TreeNode(val=root_val)

            if pre_end - pre_start == 1:
                return root

            in_o_root = in_o_dic[root_val]
            left_cnt = in_o_root - in_start
            root.left = search(
                pre_start + 1, pre_start + left_cnt + 1, in_start, in_o_root
            )
            root.right = search(
                pre_start + left_cnt + 1, pre_end, in_o_root + 1, in_end
            )
            return root

        return search(0, n, 0, n)


Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
