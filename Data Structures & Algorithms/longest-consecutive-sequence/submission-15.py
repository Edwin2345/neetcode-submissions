class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #base case -> empty list
        if len(nums) == 0:
           return 0

        #sort the list first to get conseq number beside eachother
        nums.sort()

        #scan left to right and see how long seq last
        # 2,3,4,4,5,10,20
        maxSeqLen, seqLen = 1,1
        for i in range(0, len(nums)-1):
            #next numebr is consequtive -> grow seq
            if nums[i] + 1 == nums[i+1]:
               seqLen += 1
            #next numebr is duplciate, can safely skip
            elif nums[i] == nums[i+1]:
               continue
            #next number is larger than consequtive -> restart seq here
            else:
               seqLen = 1
            maxSeqLen = max(maxSeqLen, seqLen)

        return maxSeqLen