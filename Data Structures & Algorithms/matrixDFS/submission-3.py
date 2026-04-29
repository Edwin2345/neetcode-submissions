class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        pathCount = [0]
        paths = []
        curPath = []
        visited = set()
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            #edge cases -> no path found
            if min(r,c) < 0  or r >= ROWS or c >= COLS:
                return
            if (r,c) in visited or grid[r][c] == 1:
                return
            
            #vprocess cur vertex -> chck if valid path
            curPath.append((r,c))
            visited.add((r,c))
            if (r,c) == (ROWS-1,COLS-1):            
                paths.append(list(curPath))
                curPath.pop()
                visited.remove((r,c))

                pathCount[0] += 1
                return
            
            #check neighbors
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
            
            #backtrack
            visited.remove((r,c))
            curPath.pop()
        
        dfs(0,0)
        print(paths)
        return pathCount[0]
