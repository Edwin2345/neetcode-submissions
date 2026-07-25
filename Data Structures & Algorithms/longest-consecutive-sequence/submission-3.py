class Solution:
    #sort first, the slide indices while we keep geting consetuive values
    # if streak ends, restart where we faield
    #O(NLOGN) time, O(N) spaces
    # [2,3,4,4,5,10,20]
    def longestConsecutive(self, nums: List[int]) -> int:
        #base case
        if not nums:
           return 0 

        #sort to get consecutive numebrs side by side
        nums.sort()
        maxSeqLen = 0

        target = nums[0]
        seqLen = 0
        for i in range(len(nums)):
            #skip duplicates as sequence can only break if next number not there at all
            if i > 0 and nums[i] == nums[i-1]:
               continue 

            #grow sequence
            if nums[i] == target:
               seqLen += 1
               target += 1   
               maxSeqLen = max(maxSeqLen, seqLen)
            #sequence broken, need to restart 
            else:
               seqLen = 1
               target = nums[i] + 1

        return maxSeqLen
