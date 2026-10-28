class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom up, need the i+1 and i+2 step min cost to compute min cost for ith step
        #work backwards as base case of i == len(num) cost is 0, i == len(num) - 1, cost is 1
        #O(N) TC, O(1) SC
        stepMinCosts = [cost[-1], 0]

        for i in range(len(cost) - 2, -1, -1):
            nextMinCost = stepMinCosts[0]
            stepMinCosts[0] = cost[i] + min(stepMinCosts[0], stepMinCosts[1])
            stepMinCosts[1] = nextMinCost


        #final min cost is min between staritng at step 1 vs step 0
        return min(stepMinCosts[0], stepMinCosts[1])
