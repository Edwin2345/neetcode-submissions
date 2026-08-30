class Solution:
    #Bottom Up: start with base cases and build up to later states
    def climbStairs(self, n: int) -> int:
        #use an array of size 2 to store 2 previous states
        #base cases: 1 way to climb 0 stairs, 1 way to climb 1 stair
        waysToClimb = [1,1]
        if n < 2:
           return waysToClimb[n]

        for i in range(2, n+1):
            prevWaysToClimb = waysToClimb[1]
            waysToClimb[1] = waysToClimb[1] + waysToClimb[0]
            waysToClimb[0] = prevWaysToClimb
            
        return waysToClimb[1]
               
            


         