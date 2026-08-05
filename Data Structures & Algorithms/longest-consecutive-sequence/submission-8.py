class Solution:
    #nlogn solution: sort
    # 2,3,4,4,5,10,20
    def longestConsecutive(self, nums: List[int]) -> int:
        #base case: empty nums
        if not nums:
           return 0
            
        #sort list
        maxSeqLen = 0 
        nums.sort()

        target = nums[0]
        curSeqLen = 0
        for i in range(len(nums)):
            #skip over duplicates -> doesn't affect longest conseq suquence
            if i > 0 and nums[i] == nums[i-1]:
               continue
            #current num matches the target, grow sequance, get next conseq num
            if nums[i] == target:
               curSeqLen += 1
               maxSeqLen = max(maxSeqLen, curSeqLen)
               target += 1
            #can't find conseq number, restart sequnce at cur index
            else: 
               curSeqLen = 1
               target = nums[i] + 1 

        return maxSeqLen
            