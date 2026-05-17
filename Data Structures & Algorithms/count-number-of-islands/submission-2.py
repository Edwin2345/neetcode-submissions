class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #loop throguh each cell,
        # if land and not in visited set, dfs to fully explore island
        # incremnt island count
        islandCount = 0
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
               return 
            if (r,c) in visited or grid[r][c] == "0":
               return

           #add current node to visited 
            visited.add((r,c))
             
            #explore all directions to fully explore island
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                #found a new island -> fulyl explroe its area usign dfs
                if grid[r][c] == "1" and (r,c) not in visited:
                   islandCount += 1
                   dfs(r,c) 

        return islandCount