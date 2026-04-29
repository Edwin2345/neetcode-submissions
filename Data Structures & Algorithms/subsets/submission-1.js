class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
       const subSets = [];
       const currSet = [];
       this.helper(0,nums,currSet,subSets);
       return subSets;
    }

    helper(i, nums, currSet, subSet){
       //reached the end --> add current set and return
       if(i == nums.length){
          subSet.push([...currSet]);
          return;
       }

       //Decision to add current element
       currSet.push(nums[i]);
       this.helper(i+1,nums,currSet,subSet);

       //backtrack --> Decision to not include current element
       currSet.pop();
       this.helper(i+1,nums,currSet,subSet);
    }
}
