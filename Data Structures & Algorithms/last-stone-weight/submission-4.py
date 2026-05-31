class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #turn stones into max heap
        negStones = [-s for s in stones]
        heapq.heapify( negStones )

        while len(negStones) > 1:
              #pop the largest 2 stones
              s1 = heapq.heappop( negStones ) * -1
              s2 = heapq.heappop( negStones ) * -1

              #add the remaining difference of smashing
              diff = abs(s1-s2)
              if diff > 0:
                 heapq.heappush(negStones, diff*-1 ) 

        return 0 if len(negStones) == 0 else negStones[0]*-1