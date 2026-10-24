"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        idToNode = {}
        if not head: return None
        nHead = Node(head.val, None, None)
        idToNode[id(head)] = nHead
        curr = nHead


        while head:
            nNext = None
            nRandom = None
            if head.next:
                if id(head.next) not in idToNode:
                    nNext = Node(head.next.val, None, None)  
                    idToNode[id(head.next)] = nNext
                else:
                    nNext = idToNode[id(head.next)]

            if head.random:
                if id(head.random) not in idToNode:
                    nRandom = Node(head.random.val, None, None)  
                    idToNode[id(head.random)] = nRandom
                else:
                    nRandom = idToNode[id(head.random)]
            curr.next = nNext
            curr.random = nRandom
            
            curr = curr.next
            head = head.next


        return nHead