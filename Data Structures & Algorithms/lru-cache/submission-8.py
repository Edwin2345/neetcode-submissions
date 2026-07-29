class LRUCache:
    #O(1) solutioon, keep pointers to MRU <-> Node <-> LRU
    #Use a map from key to Node for O(1) look up
    #Get: if not in nodeMap -> return -1, otehrsie, lookup Node, remove and insert it as mRU
    #Put: lookup nodeMap and remove from list if there, insert as MRU and remove LRU if at cap
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.nxt = None 

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.cap = capacity
        self.MRU = None
        self.LRU = None


    def removeFromLL(self, node):
        #update neighbors
        if node.prev:
           node.prev.nxt = node.nxt 
        if node.nxt:
           node.nxt.prev = node.prev 

        #update MRU and LRU
        if self.MRU == node:
           self.MRU = node.nxt
        if self.LRU == node:
           self.LRU = node.prev  

        #update node
        node.prev, node.nxt = None, None


    def insertMRU(self, node):
        #exisitn MRU, place node infront
        if self.MRU:
           oldMRU = self.MRU
           node.prev, node.nxt, oldMRU.prev = None, oldMRU, node
           self.MRU = node
        #list is empty, LRU and MRU are the node now
        else:
           self.MRU = node
           self.LRU = node
        

    def get(self, key: int) -> int:
        #key not in cache
        if key not in self.nodeMap:
           return -1
        
        #find node and remove from L.L
        node = self.nodeMap[key]
        self.removeFromLL(node)
         
        #insert the node as MRU
        self.insertMRU(node)
         
        return node.val
        

    def put(self, key: int, value: int) -> None:
        #if node is existing, remove from L.L
        foundNode = None
        if key in self.nodeMap:
            foundNode = self.nodeMap[key]
            self.removeFromLL(foundNode)

        #create new node if not exist or update value
        if foundNode is None:
           foundNode = self.Node(key, value)
           self.nodeMap[key] = foundNode
        else:
           foundNode.val = value  
        
        #insert as MRU
        self.insertMRU(foundNode)

        #remove LRU if over capacity
        if len(self.nodeMap) > self.cap:
           self.nodeMap.pop(self.LRU.key)
           self.removeFromLL(self.LRU)
        


        
