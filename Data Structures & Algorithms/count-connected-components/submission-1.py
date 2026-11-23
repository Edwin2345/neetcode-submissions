class Solution:
    # we can dfs every node, and have a global visited set,
    # every time we can dfs unexplored, that is a new compoinet
    # TC: O(V+E) as we visit eveyr vertice and edge once,
    # SC: O(V+E) for adj list
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build undirected adj list
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def bfs(node):
            q = deque([node])
            visited.add(node)

            while len(q) > 0:
                n = q.popleft()
                for neighbor in adj[n]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            

        # the numebr of tiems we find unexplroed node
        # is numebr of compoents
        numComponents = 0
        for node in range(n):
            if node not in visited:
                numComponents += 1
                bfs(node)

        return numComponents
