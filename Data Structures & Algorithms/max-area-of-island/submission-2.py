class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r,c):
            #edge cases -> no area to add
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            #found new land -> dfs to get entire size of island
            curArea = 1
            visited.add((r,c))
            
            curArea += dfs(r+1,c)
            curArea += dfs(r-1,c)
            curArea += dfs(r,c+1)
            curArea += dfs(r,c-1)
            
            return curArea
        
        #iterate through grid and if found new land -> dfs to get area of entire island
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea