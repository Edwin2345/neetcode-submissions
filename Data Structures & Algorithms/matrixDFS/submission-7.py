class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
         ROWS,COLS = len(grid), len(grid[0])
         allPaths = []
         path = []
         visited = set()
         numUniquePaths = 0

         def dfs(r,c):
            nonlocal numUniquePaths

            #edge cases to return early from
            if min(r,c) < 0  or r >= ROWS or c >= COLS:
               return
            if grid[r][c] == 1 or (r,c) in visited:
               return

            #process current node
            path.append((r,c))
            visited.add((r,c))

            if r == ROWS-1 and c == COLS-1 and grid[r][c] == 0:
               allPaths.append(list(path))
               numUniquePaths += 1

            #explore the neighbors
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            #backtrack
            visited.remove((r,c))
            path.pop()
         
         dfs(0,0)
         #print(allPaths)
         return numUniquePaths
             