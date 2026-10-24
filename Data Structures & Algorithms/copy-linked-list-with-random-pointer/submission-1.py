"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head  in self.map:
            return self.map[head]
        
        curr = Node(head.val)
        self.map[head] = curr
        curr.next = self.copyRandomList(head.next)
        curr.random = self.map.get(head.random)

        return curr