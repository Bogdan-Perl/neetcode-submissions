class Node:
    def __init__(self, prev, nex, val):
        self.prev, self.next = prev, nex
        self.val = val
        self.key = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(None, None, None)
        self.right = Node(self.left, None, None)
        self.left.next = self.right

    def insert(self, node):
        prev, nex = self.right.prev, self.right
        prev.next = nex.prev = node
        node.next, node.prev = nex, prev

    def remove(self, node):
        prev, nex = node.prev, node.next
        prev.next, nex.prev = nex, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(None, None, value)
            self.cache[key].key = key
            self.insert(self.cache[key])
            return
        if len(self.cache) >= self.capacity:
            LRU = self.left.next
            del self.cache[LRU.key]
            self.remove(LRU)
        self.cache[key] = Node(None, None, value)
        self.cache[key].key = key
        self.insert(self.cache[key])




        
        
