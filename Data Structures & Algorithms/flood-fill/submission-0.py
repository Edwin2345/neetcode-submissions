class Solution:
    #question: are we mutating roginal image?
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:       
        #dfs all paths to update image
        origColor = image[sr][sc]
        ROWS,COLS = len(image), len(image[0])
        visited = set()

        def dfs(r, c):
            #base cases: invalid indices
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
               return
            #base case: visted or not same color as orgiinal node   
            if (r,c) in visited or image[r][c] != origColor:
               return

            #update current node color , and add to viisted
            image[r][c] = color
            visited.add((r,c))

            #go in all 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            #backtrack
            visited.remove((r,c)) 


        dfs(sr,sc)
        return image 
