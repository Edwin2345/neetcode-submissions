class Solution:
    def climbStairs(self, n: int) -> int:
      
      cache = {}
      def countWaysToClimb(step):
         if step == n:
            return 1
         if step > n:
            return 0
         if step in cache:
            return cache[step]

         cache[step] = countWaysToClimb(step + 1) + countWaysToClimb(step + 2)
         return cache[step]
         
      return countWaysToClimb(0)