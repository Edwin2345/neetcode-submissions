class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #build a set of values
        numSet = set()
        for n in nums:
            numSet.add(n)
        
        maxSeqLen =  0
        for num in nums:
            #there is a value that consequtively preceeds num
            #skip  over num as starting here won't be the largest possible
            if num-1 in numSet:
               continue 

            #try to make largest conseq seq starting at num    
            target = num
            seqLen = 0
            while target in numSet:
                  seqLen += 1
                  target += 1
                  maxSeqLen = max(maxSeqLen, seqLen)
        
        return maxSeqLen