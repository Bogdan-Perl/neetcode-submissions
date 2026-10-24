class ListNode:

    def __init__(self, key = 0, nxt = None):
        self.key = key
        self.next = nxt


class MyHashSet:



    def __init__(self):
        self.hSet = [ListNode() for i in range(10**4)]

        

    def add(self, key: int) -> None:
        hashed = key % len(self.hSet)
        cur = self.hSet[hashed]
        
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        
        cur.next = ListNode(key)


    def remove(self, key: int) -> None:
        hashed = key % len(self.hSet)
        cur = self.hSet[hashed]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next
        

        

    def contains(self, key: int) -> bool:
        hashed = key % len(self.hSet)
        cur = self.hSet[hashed]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)