class Solution:
    # we can use union find data structe as each component is a conencted set
    class UnionFind:
        def __init__(self, n):
            self.numComponents = n
            self.parent = {}
            self.rank = {}

            for node in range(n):
                self.parent[node] = node
                self.rank[node] = 0

        def find(self, node):
            if node != self.parent[node]:
                self.parent[node] = self.find(self.parent[node])
            return self.parent[node]
        
        def union(self, node1, node2):
            root1, root2 = self.find(node1), self.find(node2)
            #already apart of same connected set
            if root1 == root2:
               return

            #if they ahve the sam rank, join to one, and inc parent rank
            if self.rank[root1] == self.rank[root2]:
               self.parent[root2] = root1
               self.rank[root1] += 1
            #otehrwsie, make the saller tree a subtree of larger to persever rank
            elif self.rank[root2] < self.rank[root1]:
               self.parent[root2] = root1
            else:
               self.parent[root1] = root2 

            #reduce numbe of compoents as e merged
            self.numComponents -= 1

        def getNumComponents(self):
            return self.numComponents 


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)

        for n1, n2 in edges:
            uf.union(n1, n2)

        return uf.getNumComponents()
