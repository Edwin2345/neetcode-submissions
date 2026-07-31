class Solution:
    #solution, use a max heap to keap track of 2 largest stones
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapify is o(N)
        maxHeap = [s*-1 for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            #get two largest stones
            s1 = heapq.heappop(maxHeap)*-1
            s2 = heapq.heappop(maxHeap)*-1

            #smash stones
            diff = s1 - s2
            if diff > 0:
               heapq.heappush(maxHeap, diff*-1) 
        
        return 0 if len(maxHeap) == 0 else maxHeap[0]*-1
        