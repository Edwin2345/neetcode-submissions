class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            #indicies are out of bound
            if min(r,c) < 0  or r >= ROWS or c >= COLS:
               return 0
            #index already visited or not is not land
            if (r,c) in visited or grid[r][c] != 1:
                return 0
            
            #found new land piece -> dfs to explore entire island and get full area
            area = 1
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                area += dfs(nr,nc)
            
            return area
         
        #iterate through every square to find max area
        for r in range(ROWS):
            for c in range(COLS): 
                maxArea = max(maxArea, dfs(r,c))

        return maxArea