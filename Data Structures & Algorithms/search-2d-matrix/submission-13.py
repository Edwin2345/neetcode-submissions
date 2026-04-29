class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix),len(matrix[0])
        L = 0
        R = ROWS*COLS-1
         
        #binary search, but convert index into 2D
        while L <= R:
              M = L + (R-L)//2
              rowM = M // COLS
              colM = M % COLS

              if matrix[rowM][colM] == target:
                 return True
              elif matrix[rowM][colM] < target:
                  L = M+1
              else:
                  R = M-1
        
        return False