class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def binarySearch(L,R):
            #base case
            if L > R:
               return False

            M = L + (R-L)//2
            M_row = M // COLS
            M_col = M % COLS

            if matrix[M_row][M_col] == target:
               return True
            elif matrix[M_row][M_col] > target:
               return binarySearch(L,M-1)
            else:
               return binarySearch(M+1,R)
      
        return binarySearch(0, ROWS*COLS-1)