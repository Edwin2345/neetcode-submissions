class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS = len(image), len(image[0])
        visited = set()
        origColor = image[sr][sc]


        def dfs(r,c):
            #base cases
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
               return
            if image[r][c] != origColor or (r,c) in visited:
               return

            #update color in current square
            image[r][c] = color
            visited.add((r,c))

            #recurse to neightbors
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)
        return image 

