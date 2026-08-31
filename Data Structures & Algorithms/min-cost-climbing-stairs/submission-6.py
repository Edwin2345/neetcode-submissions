class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Bottom up dp -> start at top of stair case and just after -> know those min cost to get to top
        #then use that to calc min cost for lower levels
        
        #store states (min cost) of the clmb one step and two steps ahead
        #base case: if at step len(cost) -> cost is 0 as at end, if at last step, min cost is cost of last step
        states = [cost[-1], 0]
         
        for i in range(len(cost)-2,-1,-1):
            costOneAhead = states[0]
            states[0] = cost[i] + min(states[0], states[1])
            states[1] = costOneAhead

        #return the min stating from either index 0 or index 1
        return min(states[0], states[1])
