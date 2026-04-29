class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        numPaths = [0]
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])

        def dfs(r,c):
            #edge cases:
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return
            if (r,c) in visited or grid[r][c] == 1:
                return
            
            #process current valid square -> see if reached end            
            if (r,c) == (ROWS-1,COLS-1):
                numPaths[0] += 1
                return
            visited.add((r,c))
            
            #dfs to explore all other possible paths from current node
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
            
            #backtrack once done
            visited.remove((r,c))

        #start at 0,0 and find all valid paths
        dfs(0,0)
        return  numPaths[0]