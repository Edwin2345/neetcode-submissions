class Solution:
    #O(N) solution, visualize this with numbe rline
    #turn nums into set, iterate throguh nums
    #if nums is start of sequence (n-1 DNE), compute the seq len
    #if if not satrt of seq skip
    #as we at most onyl visit nu 3 times (once for set construct, once when skip, once when iterating throguh seq, this is on)
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeqLen = 0

        for n in nums:
            #skip if not start of a seq
            if n-1 in numSet:
               continue

            #otherwise, calc the 
            target, curSeqLen = n, 0
            while target in numSet:
                target += 1
                curSeqLen += 1

            maxSeqLen = max(maxSeqLen, curSeqLen)

        return maxSeqLen 
        