class Solution:
    def climbStairs(self, n: int) -> int:
        #Top Down DP -> save states in cache
        cache = {}
        def countWaysToClimb(step):
            #base case: at the top alread 
            if step == n:
               return 1
            #base case: already computed the numebr of ways to get to top at this step
            if step in cache:
               return cache[step]
            #overshot the stairs:
            if step > n:
               return 0   
            
            #if not at top yet, number of ways is sum of taking 1 step now or two
            cache[step] = countWaysToClimb(step + 1) + countWaysToClimb(step + 2)
            return cache[step]
         
        return countWaysToClimb(0)
         