class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seenBefore = new Map();

        for(let num of nums){
            if(seenBefore.has(num)){
                return true;
            }

            seenBefore.set(num, num);
        }

        return false;
    }
}
