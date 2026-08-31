class Solution:
    def climbStairs(self, n: int) -> int:
      
      #store the number of ways to reach top from one step ahead or 2 steps ahead in state arr
      #base case: if step == n -> 0 ways, if step == n-1 --> 1 way (jsut take 1 step)
      state = [1,0]

      #use that to build number of ways for lower steps (sum of ways when takign 1 step from here or 2)
      for _ in range(n-1,-1,-1):
         prevNumWays = state[0]
         state[0] = state[0] + state[1]
         state[1] = prevNumWays
   
      return state[0]