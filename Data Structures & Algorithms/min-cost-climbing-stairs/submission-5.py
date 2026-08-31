class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Top Down DP: memoize the min cost at a certain step value to reahc top
        cache = {}
        def calcMinCost(step):
            #reached top of stairs
            if step == len(cost):
               return 0            
            #at the last step, only choise is to pay that cost and go one step up
            if step == len(cost)-1:
               return cost[step] + calcMinCost(step + 1)
            #already compute min cost to reach top at this step value
            if step in cache:
               return cache[step]
            
            #otherwise, cost is current step + min of choosing 1 or 2 steps
            cache[step] = cost[step] + min(
               calcMinCost(step + 1), 
               calcMinCost(step + 2)
            )

            return cache[step]
            
        #return the min stating from either index 0 or index 1
        return min(calcMinCost(0), calcMinCost(1))
