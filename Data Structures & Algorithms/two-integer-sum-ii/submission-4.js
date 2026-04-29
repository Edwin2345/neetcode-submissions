class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        
        for(let i=0; i<numbers.length-1; ++i){
            let high=numbers.length-1;
            let low=i+1;
            while(low <= high){
                let mid = low + Math.floor((high-low)/2);
                if(numbers[mid] == target-numbers[i]){
                   return [i+1, mid+1];
                }
                else if(numbers[mid] < target-numbers[i]){
                   low = mid+1;
                }
                else{
                   high = mid-1;
                }
            }
        }

        //no solution
        return [-1,-1];
    }
}
