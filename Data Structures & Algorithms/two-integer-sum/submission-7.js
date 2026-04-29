class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target){
        const numMap = new Map();

        for(let i=0; i<nums.length; ++i){

            if(numMap.has(target-nums[i])){
               return [numMap.get(target-nums[i]), i];
            }

            numMap.set(nums[i], i);
        }

        return [-1,-1];
    }
}
