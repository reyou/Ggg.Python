class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    # just remove and add item to move it at the end of the linked list
    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
    # puts a new item into hash and doubly linked list
    def put(self, key,value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key,value)
        self.add(node)
        self.dic[key] = node
        # if out of capacity remove from head (oldest)
        if len(self.dic) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dic[node.key]

    # remove node directly from the spot
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # adds as a last node
    def add(self, node):
        lastNodePointer = self.tail.prev
        lastNodePointer.next = node
        self.tail.prev = node
        node.prev = lastNodePointer
        node.next = self.tail






        

