# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        def reverse(nxt, curr):
            prev = curr.next
            curr.next = nxt
            if prev == None:
                return curr
            return reverse(curr, prev)


        # 1 -> 2 -> 3 -> None
        # None <- 1  2 -> 3 -> None

        return reverse(None, head)


