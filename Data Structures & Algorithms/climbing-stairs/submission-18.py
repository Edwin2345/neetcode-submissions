class Solution:
    def climbStairs(self, n: int) -> int:
        #top down: cache # of ways  at a step
        #O(N) TC (as compute each state once), O(N) space
        cache = {}
        def climb(i):
            #found 1 way to reach top
            if i == n:
               return 1
            #already computed number of ways
            if i in cache:
               return cache[i] 

            #at n-1 step, only choice is to take 1 step
            if i == n - 1:
               cache[i] = climb(i + 1)
               return cache[i]

            #otherwise, number of ways to climb from ith step
            #is combo of both taking 1 step her e or 2 tsteps
            cache[i] = climb(i + 1) + climb(i + 2)
            return cache[i]  
        
        #return total number of ways starting at step 0
        return climb(0)