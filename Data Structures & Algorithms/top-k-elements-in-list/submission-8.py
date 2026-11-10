class Solution:
    #answer is unique, and k is always valid
    #return in any order
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #freq count the nums
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        
        #convert map into a min heap of size k
        heap = []
        for num,freq in freqMap.items():
            heapq.heappush(heap, (freq, num)) 
            if len(heap) > k:
               heapq.heappop(heap)

        #turn heap back into answer array
        return [val for _,val in heap] 
        
