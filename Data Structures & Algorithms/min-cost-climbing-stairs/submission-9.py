class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Bottom Up Solution: store the min cost of the enxt two steps to compute current
        #base case -> if at last step - pay the cost and mvoe 1, if past last, pay nothing
        nextStepsMinCosts = [cost[-1], 0]

        for i in range(len(cost)-2, -1, -1):
            nextMinCost = nextStepsMinCosts[0]
            nextStepsMinCosts[0] = cost[i] + min(nextStepsMinCosts[0], nextStepsMinCosts[1])
            nextStepsMinCosts[1] = nextMinCost
        
        return min(nextStepsMinCosts[0], nextStepsMinCosts[1])