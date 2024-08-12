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
        # 10 ** 100
        ll1 = []
        ll2 = []
        while l1 != None:
            ll1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            ll2.append(l2.val)
            l2 = l2.next
        ans = []
        l1 = list(map(str,ll1))
        l2 = list(map(str,ll2))
        ans_string = list(map(int,reversed(str(int("".join(reversed(l1))) + int("".join(reversed(l2)))))))

        print(ans_string)
        ans = ListNode(ans_string[0])
        ans_tmp = ans
        for i in range(len(ans_string)):
            if i+1 == len(ans_string):
                ans_tmp.next = None 
                break
            ans_tmp.next = ListNode(ans_string[i + 1])
            ans_tmp = ans_tmp.next
        return ans
        


(Solution().addTwoNumbers([2,4,3],[5,6,4]))