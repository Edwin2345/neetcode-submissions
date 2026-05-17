class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            #invalid edge cases, return 0 area
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
               return 0
            if (r,c) in visited or grid[r][c] == 0:
               return 0
            
            #add current cell to island area
            area = 1
            visited.add((r,c))

            #dfs to remaing cells add accumalte island area
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                   maxArea = max(maxArea, dfs(r,c))

        return maxArea 
