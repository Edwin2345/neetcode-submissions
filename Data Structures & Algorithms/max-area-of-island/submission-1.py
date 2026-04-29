class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r,c):
            #edge cases -> not valid square to add to area
            if min(r,c) < 0 or r >= ROWS or c >= COLS: 
                return 0
            if (r,c) in visited or grid[r][c] == 0:
                return 0
            
            #add current square and get area of adjacent in island
            area = 1
            visited.add((r,c))

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            return area
        
        #iterate through grid and find area of largest possible connected island
        for r in range(ROWS):
            for c in range(COLS):
                #found new island
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea