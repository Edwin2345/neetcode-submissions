class Solution:
    #Q: if there are ties how do we settle -> A: always a uniqeu answe
    #create a map val -> [freq, val]
    #iterate throguh values of map -. use min heap and kepe track
    # map the heap vals back into values
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            if n not in freqMap:
               freqMap[n] = [1,n]
            else:
               freqMap[n][0] += 1

        minHeap = []
        for freqPair in freqMap.values():
            heapq.heappush(minHeap,freqPair)
            if len(minHeap) > k:
               heapq.heappop(minHeap)

        return [pair[1] for pair in minHeap] 