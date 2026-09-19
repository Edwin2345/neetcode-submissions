class Solution:
    #this is still a linear scan but you either skip the first house, or skip the last house
    #wrappign around makes you chekc adjacen house
    def rob(self, nums: List[int]) -> int:

        #only one house, solution is to rob that
        if len(nums) == 1:
           return nums[0] 
        
        def maxRob(index, houses, cache):
            #index out of bounds
            if index >= len(houses):
               return 0
            #already computed max rob amount for this index
            if index in cache:
               return cache[index]

            #compute max rob -> rob hosue and go to next next, or skip and go to adjacent
            cache[index] = max(
                houses[index] + maxRob(index + 2, houses, cache),  
                maxRob(index + 1, houses, cache)
            )
            return cache[index]  

        #return the max rob amount by compairng skiping the first house or the last
        return max( maxRob(0, nums[1:], {}),  maxRob(0, nums[:-1], {}) )


             