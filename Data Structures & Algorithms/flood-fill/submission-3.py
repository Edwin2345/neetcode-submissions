class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        START_COLOR = image[sr][sc]
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(r,c):
            #base cases
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
               return
            if (r,c) in visited or image[r][c] != START_COLOR:
               return

            #change squares start color to the new color
            image[r][c] = color
            visited.add( (r,c) )

            #dfs to the other squares
            for dr,dc in DIRECTIONS:
                dfs(r + dr, c + dc)

        dfs(sr,sc)
        return image
        