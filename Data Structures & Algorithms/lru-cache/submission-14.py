class LRUCache:
    # MRU -->   <--- LRU
    #have a map to look up value : Node
    #is cap always gonna be positive or 0?
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.value = val
            self.left = None
            self.right = None

    def __init__(self, capacity: int):
        self.maxCap = capacity
        self.cap = 0
        self.MRU = None
        self.LRU = None
        self.cache = {}
    
    def removeNode(self, node):
        #only node
        if self.MRU == node and self.LRU == node:
           self.MRU, self.LRU = None, None
        #removing MRU
        elif self.MRU == node:
           self.MRU = node.right
           node.right.left = None
        #removing LRU
        elif self.LRU == node:
           self.LRU = node.left
           node.left.right = None
        #removing from the middle
        else:
            node.left.right = node.right
            node.right.left = node.left    

        #clear the deleted nodes won points
        node.left = None
        node.right = None    
    
    def insertMRU(self, node):
        #no node, just add it
        if self.MRU is None and self.LRU is None:
           self.MRU, self.LRU = node, node 
           return
        
        #otherwise insert between MRU pointer and current MRU node (tmp)
        tmp = self.MRU
        self.MRU, tmp.left = node, node
        node.left, node.right = None, tmp
   
    def get(self, key: int) -> int:
        #key not found
        if key not in self.cache:
           return -1

        #move node to MRU and return valid
        self.removeNode(self.cache[key])
        self.insertMRU(self.cache[key])
        return self.cache[key].value 
        
    def put(self, key: int, value: int) -> None:
        #key already exists
        if key in self.cache:
           self.cache[key].value = value
           self.removeNode(self.cache[key])
           self.insertMRU(self.cache[key])
           return
        
        #over capacity, remove LRU first
        if self.cap == self.maxCap:
           del self.cache[ self.LRU.key ]
           self.removeNode( self.LRU )
           self.cap -= 1

        #add new node as MRU
        self.cache[key] = self.Node(key, value)
        self.insertMRU(self.cache[key]) 
        self.cap += 1
        
