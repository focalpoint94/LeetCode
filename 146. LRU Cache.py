class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            ret = self.dict.pop(key)
            self.dict[key] = ret
            return ret
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            self.dict[key] = value
        else:
            if len(self.dict) == self.capacity:
                self.dict.pop(next(iter(self.dict)))
            self.dict[key] = value
        


# class Node:

#     def __init__(self, key=None, val=None, prv=None, nxt=None):
#         self.key = key
#         self.val = val
#         self.prv = prv
#         self.nxt = nxt


# class DoublyLL:

#     def __init__(self):
#         self.head = Node()
#         self.tail = Node()
#         self.head.nxt = self.tail
#         self.tail.prv = self.head

#     def insertTail(self, node):
#         prv = self.tail.prv
#         prv.nxt = node
#         node.prv = prv
#         node.nxt = self.tail
#         self.tail.prv = node

#     def deleteNode(self, node):
#         prv = node.prv
#         nxt = node.nxt
#         prv.nxt = nxt
#         nxt.prv = prv

#     def popHead(self):
#         node = self.head.nxt
#         nxt = node.nxt
#         nxt.prv = self.head
#         self.head.nxt = nxt
#         return node



# class LRUCache:

#     def __init__(self, capacity: int):
#         self.q = DoublyLL()
#         self.dict = {}
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key in self.dict:
#             node = self.dict[key]
#             self.q.deleteNode(node)
#             self.q.insertTail(node)
#             return node.val
#         else:
#             return -1        

#     def put(self, key: int, value: int) -> None:
#         if key in self.dict:
#             node = self.dict[key]
#             self.q.deleteNode(node)
#             self.q.insertTail(node)
#             node.val = value
#         else:
#             if len(self.dict) == self.capacity:
#                 node = self.q.popHead()
#                 self.dict.pop(node.key)
#             node = Node(key, value)
#             self.q.insertTail(node)
#             self.dict[key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
