class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up: each step depends on the 2 steps ahead to compute numways
        #O(N) TC (as compute each state once), O(1) space

        #base case, at nth step there is 1 way (found it)
        #at n-1 th step there is 1 way (take 1 step)
        numWays = [1,1]

        for _ in range(n-2,-1,-1):
            nextStepWays = numWays[0]
            curStepWays = numWays[0] + numWays[1]
            numWays[0] = curStepWays
            numWays[1] = nextStepWays
        
        return numWays[0]
       