class Solution:
    def helper(self, grid, r, c, visited):
        #EDGE CASES -> no valid paths
        #index out of bounds 
        ROWS,COLS = len(grid), len(grid[0])
        if min(r,c)<0 or r>=ROWS or c>=COLS:
            return 0
        #r,c is blocked or already visited
        if grid[r][c] == 1 or (r,c) in visited :
            return 0

        #Found a valid path to end
        if r == ROWS-1 and  c == COLS-1 and grid[r][c]==0:
            return 1
        
        #add current vertex and rec compute number of valid paths in the 4 directions
        count = 0
        visited.add((r,c))
        count += self.helper(grid, r+1, c, visited)
        count += self.helper(grid, r-1, c, visited)
        count += self.helper(grid, r, c+1, visited)
        count += self.helper(grid, r, c-1, visited)

        #backtrack and return count freom this node
        visited.remove((r,c))
        return count

    def countPaths(self, grid: List[List[int]]) -> int:
        #keep track of visited nodes to ensure we don't
        visited = set()

        return self.helper(grid,0,0,visited)