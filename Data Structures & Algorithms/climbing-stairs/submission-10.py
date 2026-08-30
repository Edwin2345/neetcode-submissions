class Solution:
    #top down: cache itnermediate states (nymber of ways to climb at smaller step size)
    #O(N) time as compute climb stars for 1..,n total steps at most once
    #O(N) space for call stack
    def climbStairs(self, n: int) -> int:

        def countWaysToClimb(totalSteps, cache):
            #foudn valid path
            if totalSteps == n:
               return 1
            #went over the count -> not valid path
            if totalSteps > n:
               return 0
            #already computed numebr of ways to climb
            if totalSteps in cache:
               return cache[totalSteps]

            #otehrwise, check numebr ways by takign either 1 or 2 steps at this point
            #cache result for later
            cache[totalSteps] = countWaysToClimb(totalSteps + 1, cache) + countWaysToClimb(totalSteps + 2, cache)
            return cache[totalSteps]
        
        return countWaysToClimb(0,{})
         

               
            


         