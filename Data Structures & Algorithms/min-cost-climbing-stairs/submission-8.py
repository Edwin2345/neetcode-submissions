class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Top Down Solution: cache the min cost of intermediate steps
        cache = {}
        def findMinCost(step):
            #already past the top of staircase
            if step == len(cost):
               return 0
            #already computed min cost at that step
            if step in cache:
               return cache[step] 
            #at the last step -> only choice is to pay current and step 1 more
            if step == len(cost) - 1:
               cache[step] = cost[step] + findMinCost(step + 1)
               return cache[step]

            #if not at top, min cost is pay current cost and the min of taking 1 or 2 steps
            cache[step] = cost[step] + min( findMinCost(step + 1), findMinCost(step + 2) ) 
            return cache[step]
        
        #can start at step 0 or step 1:
        return  min( findMinCost(0), findMinCost(1) )