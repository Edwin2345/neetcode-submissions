class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:
    '''
     hashmap to store key, node pair
     LL with LRU, and MRU node -> FIXED IN PLACE
     get -> check if in hashmap, remove node from LL, insertMRU
     put -> create node, if key exist remove existing node, insertMRU + add to cache, if at capevict LRU

     MRU <-> LRU
     MRU <-> n1 <-> LRU
     MRU <-> n2 <-> n1 <-> LRU
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.MRU = Node(0,0)
        self.LRU = Node(0,0)
        self.cache = {}
        self.MRU.nxt = self.LRU
        self.LRU.prev = self.MRU

    def Remove(self,node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
    
    def InsertMRU(self,node):
        oldMRU = self.MRU.nxt
        #update pointers to node
        self.MRU.nxt = node
        oldMRU.prev = node
        #update node's pointers
        node.nxt = oldMRU
        node.prev = self.MRU
               
    def get(self, key: int) -> int:
        if key in self.cache:
           #set accessed node to be MRU in LL
           self.Remove(self.cache[key])
           self.InsertMRU( self.cache[key])
           #return value
           return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key,value)

        #remove if already exists -> no duplicates in LL
        if key in self.cache:
            self.Remove(self.cache[key])
        
        #insert new node
        self.cache[key] = newNode
        self.InsertMRU(newNode)

        #remove LRU if capacity reached
        if len(self.cache) > self.capacity:
            del self.cache[self.LRU.prev.key]
            self.Remove(self.LRU.prev)
        
        
             
        
