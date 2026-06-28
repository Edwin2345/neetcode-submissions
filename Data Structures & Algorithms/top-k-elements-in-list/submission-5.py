class Solution:
    #Q: always gonna be an aswer? (K <= # of unique)
    #P: Linear solution is to use bucket sort
    #P: make freqMap, and 2d list of len(nums)
    #P: indices are the freq -> values are list of nums with that freq
    #P: once done building list, iterate in reverse and take top k
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freqList = [[] for _ in range(len(nums)+1)]
        topKList = []

        #count freq
        for n in nums:
            if n in freqMap:
               freqMap[n] += 1
            else:
               freqMap[n] = 1 
        
        #insert into "bucket" of freqList -> index is frequency
        for n,freq in freqMap.items():
            freqList[freq].append(n)

        #take the top k
        for freq in range(len(nums), 0, -1):
            for n in freqList[freq]:
                topKList.append(n)
                if len(topKList) == k:
                   return topKList 


        