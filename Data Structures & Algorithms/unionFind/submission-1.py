class UnionFind:
    # we have n elements labeled 0 to n-1
    #TC: ROUGHLY O(1) for both operations due to rank and path compression 
    #SC:  O(N) where N is the numebr of elements
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.numComponents = n

        #initialize evey elemtn as aprent of itslef with no rank (tree height)
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    #return the parent of x --> the representative set item (which is parent of itself (root))
    #do path compression at same time
    def find(self, x: int) -> int:
        if x != self.parent[x]:
           self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        #find both representative set items, if the same they are apart of same set
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
           return False 
        
        #otherwise, uinon the sets by adjusting their parents 
        #if equal ehgiths, pick oen, and make the new parents rank (height) one more
        if self.rank[rootX] == self.rank[rootY]:
           self.parent[rootY] = rootX
           self.rank[rootX] +=1  
        #attach shorter tree set under larger tree set so total rank (height stays) same
        elif self.rank[rootY] < self.rank[rootX]:
           self.parent[rootY] = rootX
        else:
           self.parent[rootX] = rootY
        
        #shrink component count
        self.numComponents -= 1
        
        return True


    def getNumComponents(self) -> int:
        return self.numComponents
