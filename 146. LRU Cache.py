class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.cnt = 0
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if self.cnt == self.capacity:
                self.cache.pop(next(iter(self.cache)))
                self.cnt -= 1
            self.cache[key] = value
            self.cnt += 1

# class DLinkedNode():
#     def __init__(self, key=None, val=None, prv=None, nxt=None):
#         self.key = key
#         self.val = val
#         self.prv = prv
#         self.nxt = nxt

# class DLinkedList():
#     def __init__(self):
#         self.head, self.tail = DLinkedNode(), DLinkedNode()
#         self.head.nxt, self.tail.prv = self.tail, self.head

#     def insertHead(self, node):
#         node.prv, node.nxt = self.head, self.head.nxt
#         self.head.nxt.prv = node
#         self.head.nxt = node
#         return node

#     def removeNode(self, node):
#         node.nxt.prv = node.prv
#         node.prv.nxt = node.nxt
#         return node

#     def removeTail(self):
#         return self.removeNode(self.tail.prv)

#     def movetoHead(self, node):
#         return self.insertHead(self.removeNode(node))


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.list = DLinkedList()
#         self.address = dict()
#         self.capacity = capacity
#         self.cnt = 0

#     def get(self, key: int) -> int:
#         if key not in self.address:
#             return -1
#         node = self.address[key]
#         self.address[key] = self.list.movetoHead(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.address:
#             node = self.address[key]
#             node.val = value
#             self.address[key] = self.list.movetoHead(node)
#         else:
#             if self.cnt == self.capacity:
#                 self.address.pop(self.list.removeTail().key)
#                 self.cnt -= 1
#             self.address[key] = self.list.insertHead(DLinkedNode(key, value))
#             self.cnt += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
