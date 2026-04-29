class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        visited = set()
        ROWS,COLS = len(grid),len(grid[0])

        def dfs(r,c):
            #edge case: oob
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            #edge case: already seen or water
            if grid[r][c] == "0" or (r,c) in visited:
                return 0
            
            #found new island -> add all children to visited, and return 1 for new island
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return 1
         
        #iterate through grid 
        for r in range(ROWS):
            for c in range(COLS):
                islandCount += dfs(r,c)

        return islandCount