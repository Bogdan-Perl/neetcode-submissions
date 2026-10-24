# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(node1, node2):
            p1, p2 = node1, node2
            ordered = ListNode()
            curr = ordered
            while p1 and p2:
                if p1.val <= p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            curr.next = p1 or p2

            return ordered.next

        def mergeSort(s,e):
            if e==s:
                return lists[s]
            if s+e+1 < 1:
                return None

 
            m = (s+e)//2 #5//2 = 2
            left = mergeSort(s, m) # 0, 2; 0, 1; 0, 0
            right = mergeSort(m+1, e) #3, 5
            merged = merge(left, right)

            return merged
        if not lists:
            return None
        return mergeSort(0, len(lists)-1)
        

