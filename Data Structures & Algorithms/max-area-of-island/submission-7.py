class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        NUM_ROWS, NUM_COLS, DIRECTIONS = len(grid), len(grid[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c):
            # edge cases:
            if min(r, c) < 0 or r >= NUM_ROWS or c >= NUM_COLS:
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            # add current land square to area of island and mark as visited
            islandArea = 1
            visited.add((r, c))

            # explore the rest of island in all directions
            for dr, dc in DIRECTIONS:
                islandArea += dfs(r + dr, c + dc)

            return islandArea
        
        #check all unvisted land squares, and fully dfs to get island size
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                   islandArea = dfs(r,c)
                   maxArea = max(maxArea, islandArea) 

        return maxArea
