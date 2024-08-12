# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans_tmp = ListNode()
        ans = None
        is_first = True
        next_digit = 0
        while l1 or l2:
            if l1 == None:
                l1_value = 0
            else:
                l1_value = l1.val 
                l1 = l1.next 
            if l2 == None:
                l2_value = 0
            else:
                l2_value = l2.val 
                l2 = l2.next 
            quotient,remainder = divmod(l1_value + l2_value + next_digit,10)
            ans_tmp.next = ListNode(remainder,None)
            next_digit = quotient
            if is_first:
                is_first = False
                ans = ans_tmp.next
            ans_tmp = ans_tmp.next
        if next_digit:
            ans_tmp.next = ListNode(next_digit)
        return ans