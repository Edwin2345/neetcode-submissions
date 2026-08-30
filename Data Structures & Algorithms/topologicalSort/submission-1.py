class Solution:
    
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        #build adj list -> {node: [neigh]}
        adj = {} 
        for i in range(n):
            adj[i] = [] 
        for src, dst in edges:
            adj[src].append(dst)

        #run preorder ds on eveyr node in graph to build toplogical order
        visitedSet = set()
        pathSet = set()
        topOrder = []
        for node in adj.keys():
            if not self.dfs(node, adj, visitedSet, pathSet, topOrder):
               return []

        #reverse to get correct topOrder
        topOrder.reverse()
        return topOrder
 

    def dfs(self, node, adj, visitedSet, pathSet, topOrder):
        #edge case: cycle detected
        if node in pathSet:
           return False
        #base case: node already added to topOrder
        if node in visitedSet:
           return True

      #add current node to path and recurse to children
        pathSet.add(node)
        for nei in adj[node]:
            if not self.dfs(nei, adj, visitedSet, pathSet, topOrder):
               return False

        #add node to topological  order, mark as visited and remove from path
        topOrder.append(node)
        visitedSet.add(node)
        pathSet.remove(node)
        return True
        

    

