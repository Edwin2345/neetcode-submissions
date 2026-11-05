class Solution:
    #treat 2d array as 1d by covertign to index = r*c-1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        NUM_ROWS, NUM_COLS = len(matrix), len(matrix[0])
        L, R = 0, NUM_ROWS*NUM_COLS - 1

        while L <= R:
            M = L + (R - L)//2
            #nmumebr of columsn == how many elements in a row
            rowM = M // NUM_COLS
            colM = M % NUM_COLS

            if matrix[rowM][colM] == target:
               return True
            elif  matrix[rowM][colM] > target:
               R = M - 1
            else:
               L = M + 1

        return False
