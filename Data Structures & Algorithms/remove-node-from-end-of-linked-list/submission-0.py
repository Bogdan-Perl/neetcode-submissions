# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)

        curr = head
        prev = dummy
        idx = length - n 
        i = 0
        while i != idx:
            i += 1
            prev = curr
            curr = curr.next

        nxt = curr.next
        prev.next = nxt
        return dummy.next










