class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])

        def dfs(r,c):
            #edge cases
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if (r,c) in visited or grid[r][c] == '0':
                return 0
            
            #dfs to explore entire island
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
            
            #retrun 1 for new island found
            return 1
       
        #iterate through grid to find new islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islandCount += dfs(r,c)
        
        return islandCount