class LRUCache:
    #brute force: use a list holding [key, val]: first index is MRU, last index is LRU
    #get: search for it, then pop at that index and push to front O(n)
    #put: add at front if over capicty pop the back O(n)
    def __init__(self, capacity: int):
        self.lst = []
        self.cap = capacity

    def get(self, key: int) -> int:
        #search for key, pop at that position and push to front (MRU)
        for i in range(len(self.lst)):
            if self.lst[i][0] == key:
               node = self.lst.pop(i)
               self.lst.insert(0, node)
               return node[1]
        #not found
        return -1
        
    def put(self, key: int, value: int) -> None:
        #if node already exist; find it, pop, and update the value
        foundNode = None
        for i in range(len(self.lst)):
            if self.lst[i][0] == key:
               foundNode = self.lst.pop(i)
               foundNode[1] = value
               break
        
        #otherwise, create it from scratch
        if foundNode is None:
           foundNode = [key, value]

        #insert as MRU, and if over capacity, pop the LRU
        self.lst.insert(0,foundNode)
        if len(self.lst) > self.cap:
           self.lst.pop() 
        
        

        
