class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        landSet = set()
        maxArea = 0
        ROWS,COLS = len(grid),len(grid[0])

        def dfs(r,c):
            #recursive edge cases -> don't add to size
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if (r,c) in landSet or grid[r][c] == 0:
                return 0
            
            #new island -> use dfs to get size
            size = 1
            landSet.add((r,c))

            size += dfs(r+1,c)
            size += dfs(r-1,c)
            size += dfs(r,c+1)
            size += dfs(r,c-1)

            return size

        #iterate through grid
        for r in range(ROWS):
            for c in range(COLS):
                #found new island
                if grid[r][c] == 1 and (r,c) not in landSet:
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea