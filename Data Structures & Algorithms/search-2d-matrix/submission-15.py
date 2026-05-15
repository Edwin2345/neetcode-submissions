class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        L = 0
        R = ROWS*COLS - 1

        while L <= R:
            mid = L + (R-L) // 2
            rowIndex = mid // COLS 
            colIndex = mid % COLS

            if matrix[rowIndex][colIndex] == target:
               return True
            elif  matrix[rowIndex][colIndex] < target:
               L = mid + 1
            else:
               R = mid - 1                  

        return False