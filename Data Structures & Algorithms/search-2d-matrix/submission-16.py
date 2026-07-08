class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        L,R = 0, ROWS*COLS-1

        while L <= R:
            M = L + (R-L)//2
            M_row = M // COLS
            M_col = M % COLS

            if matrix[M_row][M_col] == target:
               return True
            elif matrix[M_row][M_col] > target:
               R = M-1
            else:
               L = M+1
        
        return False