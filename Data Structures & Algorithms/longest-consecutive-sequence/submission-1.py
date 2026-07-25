class Solution:
    #brute force: turn nums into a set for O(1) lookup
    #iterate throguh every num, take it as starting point
    #continue to incrment cur while we found consecutive numbers
    #update global max lenght variable
    #O(N^2) time, O(N) spaces
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn nums into set as we dont care about duplicates and O(1) lookup
        numSet = set(nums)
        maxSeqLen = 0

        for n in nums:
            seqLen = 0
            target = n
            while target in numSet:
                seqLen += 1
                target += 1                
            maxSeqLen = max(maxSeqLen, seqLen)
        
        return maxSeqLen
