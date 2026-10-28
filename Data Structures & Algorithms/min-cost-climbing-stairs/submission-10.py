class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #top down: use a cache O(N) time O(N) space
        cache = {}
        def calcMinCost(i):
            # reached last step -> no more cost
            if i == len(cost):
                return 0
            #already computed
            if i in cache:
               return cache[i]  
            # at last step --> only choice is to take 1 step
            if i == len(cost) - 1:
                cache[i] = cost[i] + calcMinCost(i + 1)
                return cache[i]

            # otherwise, min cost is current cost + min of the choice
            # between taking one or stow steps
            cache[i] =  cost[i] + min(calcMinCost(i + 1), calcMinCost(i + 2))
            return cache[i]

        # min cost is the min betweeen starting at 0 or 1 index floor
        return min(calcMinCost(0), calcMinCost(1))
