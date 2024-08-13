import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyTreeNode:
    def __init__(self, val=0, left=None, right=None, par=None):
        self.val = val
        self.left = left
        self.right = right
        self.par = par


class Solution:
    def btreeGameWinningMove(self, root, n: int, x: int) -> bool:
        root = self.makeMyTree(root)
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue

            if node.val == x:
                break

            queue.append(node.left)
            queue.append(node.right)

        a = self.countNode(node.left, node)
        b = self.countNode(node.right, node)
        c = self.countNode(node.par, node)

        if a > b + c + 1:
            return True
        if b > a + c + 1:
            return True
        if c > a + b + 1:
            return True
        return False

    def countNode(self, root, enemyRoot):
        cnt = 0
        if root is None:
            return 0
        visited = [0 for _ in range(101)]
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            if visited[node.val] or node.val == enemyRoot.val:
                continue
            cnt += 1
            visited[node.val] = 1
            queue.append(node.left)
            queue.append(node.right)
            queue.append(node.par)
        return cnt

    def makeMyTree(self, root):
        def dfs(node, par):
            if node == None:
                return None
            mynode = MyTreeNode(node.val)
            mynode.left = dfs(node.left, mynode)
            mynode.right = dfs(node.right, mynode)
            mynode.par = par
            return mynode

        return dfs(root, None)
