class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seenBefore = {};

        for(let num of nums){
            if(seenBefore[num] == num){
                return true;
            }
            seenBefore[num] = num;
        }

        return false;
    }
}
