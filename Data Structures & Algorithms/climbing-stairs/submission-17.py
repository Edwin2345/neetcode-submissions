class Solution:
    def climbStairs(self, n: int) -> int:
        #Bottom Up DP -> use the next 2 steps number of ways to comptue the current steps numebr of ways
        #base case: at step = n-1 -> 1 way, at step n -> 1 way
        numWaysToClimb = [1,1]

        #compute this value for step 0 (bottom of stairs)
        for _ in range(n-2,-1,-1):
            nextStepNumWays = numWaysToClimb[0]
            numWaysToClimb[0] =  numWaysToClimb[0] + numWaysToClimb[1]
            numWaysToClimb[1] = nextStepNumWays 

        return numWaysToClimb[0]
         