class Solution:
    # we need a DS to keep track of which nodes are connected to eachother (in the same set)
    # specifically process an edge one by one and if the edge connects to a node already
    # in the same set, we have found the redundant connection
    # union find ds, iterate throguh each edge and union the nodes as they are apart of connected set
    #TC: O(N) as initinaliztion is every node, and we call O(1) union N times for N edges
    #SC: O(N) for n nodes in union find DS
    class UnionFind:
        #initialize each parent as itself, and 
        def __init__(self, n):
            self.rank = [0]*(n+1)
            self.parent = [i for i in range(n+1)]
        
        #path compression and find the set representative element (root)
        def find(self, n):
            if n != self.parent[n]:
               self.parent[n] = self.find(self.parent[n]) 
            return self.parent[n]
        
        def union(self, n1, n2):
            #find roots, and see if they are already part of same set
            root1, root2 = self.find(n1), self.find(n2)
            if root1 == root2:
               return False 
            
            #if both have same rank, pick one and increase it
            if self.rank[root1] == self.rank[root2]:
               self.parent[root2] = root1
               self.rank[root1] += 1
            #otherwise add it to the smaller root
            elif self.rank[root2] < self.rank[root1]:
               self.parent[root2] = root1
            else:
               self.parent[root1] = root2

            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = self.UnionFind(len(edges))

        for n1,n2 in edges:
            if not uf.union(n1,n2):
               return [n1,n2] 
        
        #shouldn't be reachable but just in case
        return []

        