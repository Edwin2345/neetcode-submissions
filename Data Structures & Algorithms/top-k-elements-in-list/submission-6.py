class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)        
        for n in nums:
            freqMap[n] += 1
        
        freqList = [[] for _ in range(len(nums)+1)]
        for n,freq in freqMap.items():
            freqList[freq].append(n)
        
        topK = []
        for freq in range(len(nums),0,-1):
            if len( freqList[freq] ) > 0:
               for n in freqList[freq]:
                   topK.append(n)
                   if len(topK) == k:
                      return topK
        
        # return empty if not possible
        return []
        
        
