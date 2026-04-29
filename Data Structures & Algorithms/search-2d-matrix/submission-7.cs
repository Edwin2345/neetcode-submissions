public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int low = 0;
        int high = matrix.Length*matrix[0].Length-1;

        while(low <= high){
            int mid = low + (high-low)/2;
            int rowMid = mid / matrix[0].Length;
            int colMid = mid % matrix[0].Length;

            if(matrix[rowMid][colMid] == target){
                return true;
            }
            else if(matrix[rowMid][colMid] < target){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }


        return false;
    }
}
