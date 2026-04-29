class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const m = matrix.length;
        const n = matrix[0].length;

        let low=0;
        let high=m*n-1;

        while(low <= high){
            let mid = low + Math.floor((high-low)/2);

            let row = Math.floor(mid / n);
            let col = mid % n;

            if(matrix[row][col] == target){
                return true;
            }
            else if(matrix[row][col] < target){
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }

        return false;
    }
}
