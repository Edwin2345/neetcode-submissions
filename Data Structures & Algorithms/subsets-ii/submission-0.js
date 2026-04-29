class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums){

        nums.sort();

        const subSets = [];
        const currSet = [];
        this.helper(0, nums, currSet, subSets);
        return subSets;
    }

    helper(i, nums, currSet, subSets){
        //reached end of decision tree --> copy over curr subSet
        if(i == nums.length){
            subSets.push([...currSet]);
            return;
        }

        //Decision to include current element
        currSet.push(nums[i]);
        this.helper(i+1,nums,currSet,subSets);

        //Backtrack --> pop and Skip Duplicates and don't take
        currSet.pop();
        while(i < nums.length-1 && nums[i] == nums[i+1]){
            ++i;
        }
        this.helper(i+1,nums,currSet,subSets);
    }
}
