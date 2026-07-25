class Solution:
    #O(N) solution -> put nums into set and iterate through
    #if num is start of a sequence (num-1 does not exist), try to grow it
    def longestConsecutive(self, nums: List[int]) -> int:
        #use set for existance checks
        numSet = set(nums)
        maxSeqLen = 0

        for n in numSet:
            #skip if not the start of a sequence
            if n-1 in numSet:
               continue

            #otherwise, compute sequence length
            seqLen = 0 
            target = n
            while target in numSet:
                seqLen += 1
                target += 1
                maxSeqLen = max(maxSeqLen, seqLen)

        return maxSeqLen
        