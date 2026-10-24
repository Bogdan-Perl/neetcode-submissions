# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse( head, None)


    def reverse(self, current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev


        return self.reverse(next_node, current)
        