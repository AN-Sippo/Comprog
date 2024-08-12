# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1, root2):
        if root1 is None and root2 is None:
            return True 
        if root1 is None or root2 is None:
            return False 
        if root1.val != root2.val:
            return False
        queue = [[root1,root2]]
        while queue:
            # ここで取り出したnodeに対して、node.leftとnode.rightをflipを行って一致させることができるならflipして次へ。
            # flipでもどうしようもないならreturn False
            root1,root2 = queue.pop()
            l1 = root1.left 
            r1 = root1.right 
            l2 = root2.left 
            r2 = root2.right
            if self.same_node(l1,l2) and self.same_node(r1,r2):
                if l1 is not None:
                    queue.append([l1,l2])
                if r1 is not None:
                    queue.append([r1,r2])
            elif self.same_node(l1,r2) and self.same_node(r1,l2):
                if l1 is not None:
                    queue.append([l1,r2])
                if r1 is not None:
                    queue.append([r1,l2])
            
            else:
                return False 
        
        return True


    
    def same_node(self,node1,node2):
        if node1 is None and node2 is None:
            return True 
        if node1 is None or node2 is None:
                return False 
        return node1.val == node2.val
        
