class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #edge case -> only 1 stone
        if len(stones) == 1:
            return stones[0]
        
        #turn stones into a max heap
        negstones = [-1*n for n in stones]
        heapq.heapify(negstones)

        while len(negstones) > 1:
            #pop off top 2 heavies stones
            s1 = -1*heapq.heappop(negstones)
            s2 = -1*heapq.heappop(negstones)
            
            #if there equal, we continue as they are already destoried
            if s1 == s2:
                continue
            #otherwise, larger stone gets smashed
            elif s2 < s1:
                s1 = s1-s2
            
            #re insert smashed stone
            heapq.heappush(negstones,-1*s1)
        
        #return last or no stones
        if len(negstones) == 1:
            return -1*negstones[0]
        else:
            return 0