# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        def swap(current):
            if not current:
                return
            if not current.next:
                return current
            next_node = current.next
            current.next = swap(next_node.next)
            next_node.next = current
            return next_node

        ans = swap(head)
        return ans
