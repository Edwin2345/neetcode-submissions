class Solution:
    # we can dfs every node, and have a global visited set,
    # every time we can dfs unexplored, that is a new compoinet
    #TC: O(V*(V+E)) as we dfs every node, SC: O(V+E) for adj list
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build undirected adj list
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        visited = set()
        def dfs(node):
            #process node
            visited.add(node)

            #recurse to neighbors
            for neighbor in adj[node]:
                if neighbor not in visited:
                   dfs(neighbor) 
        
        numComponents = 0
        for node in range(n):
            if node not in visited:
               numComponents += 1
               dfs(node) 

        return numComponents
        