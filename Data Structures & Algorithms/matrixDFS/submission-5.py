class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        paths = []
        curPath = []
        visited = set()
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            #edge cases -> no path found
            if min(r,c) < 0  or r >= ROWS or c >= COLS:
                return 0
            if (r,c) in visited or grid[r][c] == 1:
                return 0
            
            #vprocess cur vertex -> chck if valid path
            curPath.append((r,c))
            visited.add((r,c))
            count = 0
            if (r,c) == (ROWS-1,COLS-1):            
                paths.append(list(curPath))                                
                count += 1
            
            #check neighbors
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                count += dfs(nr,nc)
            
            #backtrack
            visited.remove((r,c))
            curPath.pop()

            return count
        
        pathCount = dfs(0,0)
       # print(paths)
        return pathCount
