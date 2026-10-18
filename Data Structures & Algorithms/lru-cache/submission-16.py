class LRUCache:
    # use a dict to map key to Node
    # doubly LL for LRU, MRU lookup --> MRU > N <> N <> N < LRU (MRU and LRU are pointer to nodes)
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.MRU = None
        self.LRU = None
        self.cache = {}

    def removeNode(self, node):
        # node is the only in list
        if self.MRU == self.LRU == node:
           self.MRU = None
           self.LRU = None
        # node is MRU
        elif self.MRU == node:
           self.MRU = self.MRU.next
           node.next.prev = None
        #node is LRU
        elif self.LRU == node:
           self.LRU = self.LRU.prev   
           node.prev.next = None
        #node is between two others
        else:
           node.prev.next = node.next
           node.next.prev = node.prev

        #clean up nodes own next and prev points
        node.next = None
        node.prev = None
    
    def insertMRU(self, node):
        #list empty
        if self.MRU == None:
           self.MRU = node
           self.LRU = node
           return

        #othwerse insert it infront of current MRU
        node.next = self.MRU
        self.MRU.prev = node

        self.MRU = node
        node.prev = None 

    def get(self, key: int) -> int:
        #key not found
        if key not in self.cache:
           return -1 

        #get value, remove node, and insert as mru
        val = self.cache[key].val
        self.removeNode( self.cache[key] )
        self.insertMRU( self.cache[key] )
        return val

    def put(self, key: int, value: int) -> None:
        #key already present -> update value in map, remove node, add as MRU
        if key in self.cache:
           self.cache[key].val = value
           self.removeNode( self.cache[key] )
           self.insertMRU( self.cache[key] ) 
           return

        #not enough space, remove from map, remove LRU, decrement count
        if self.count == self.capacity:
           del self.cache[self.LRU.key]
           self.removeNode( self.LRU )
           self.count -= 1 

        #add new key -> create node, increment count, add to map, and insert as MRU
        newNode = self.Node(key, value)
        self.cache[key] = newNode
        self.insertMRU( newNode )
        self.count += 1

