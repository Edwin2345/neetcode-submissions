class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix)*len(matrix[0]) - 1

        while( L <= R):
            M = L + (R - L)//2
            row = M // (len(matrix[0]))
            col = M % (len(matrix[0]))
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                L = M + 1
            else:
                R = M - 1
        
        return False