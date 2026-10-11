class Solution:
    #straight line --> once we reach end we are done
    #start with decision tree
    def rob(self, nums: List[int]) -> int:

        cache = {}
        def calcMaxRob(i):
            #past the last house
            if i >= len(nums):
               return 0
            #already computed max rob amount
            if i in cache:
               return cache[i] 

            #return max rob of 2 possible decisions
            #rob curent and go next next or just rob next
            cache[i] = max(nums[i] + calcMaxRob(i+2),calcMaxRob(i+1))
            return cache[i] 
        
        return calcMaxRob(0)

        