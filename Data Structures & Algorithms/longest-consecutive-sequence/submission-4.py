class Solution:
    #brute force -> iterate through each element and treat as starting point in sequene
    #use a set, as just need to ensure next num exists
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeqLen = 0

        for n in nums:
            target = n
            seqLen = 0
            while target in numSet:
                seqLen += 1
                target += 1
                maxSeqLen = max(maxSeqLen, seqLen)

        return maxSeqLen
        
        