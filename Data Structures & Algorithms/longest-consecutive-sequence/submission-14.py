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
        for i in range(1, len(nums)):
            #next numebr is consequtive -> grow seq
            if nums[i - 1] + 1 == nums[i]:
               seqLen += 1
            #next numebr is duplciate, can safely skip
            elif nums[i - 1] == nums[i]:
               continue
            #next number is larger than consequtive -> restart seq here
            else:
               seqLen = 1
            maxSeqLen = max(maxSeqLen, seqLen)

        return maxSeqLen