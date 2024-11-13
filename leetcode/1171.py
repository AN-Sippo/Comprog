# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode):
        sums = [[]]
        current = head

        ans = []

        def pop(found_idx):
            for _ in range(found_idx + 1):
                sums.pop()
                ans.pop()

        while current:
            if current.val == 0:
                current = current.next
                continue
            next_arr = [current.val]
            for i, val in enumerate(sums[-1]):
                next = val + current.val
                next_arr.append(next)
                if next == 0:
                    pop(i)
                    break
            else:
                sums.append(next_arr)
                ans.append(current)

            current = current.next

        if not ans:
            return None

        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]
        ans[-1].next = None

        return ans[0]
