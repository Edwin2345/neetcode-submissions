class Solution:
    #this is still a linear scan but you either skip the first house, or skip the last house
    #wrappign around makes you chekc adjacen house
    def rob(self, nums: List[int]) -> int:

        #only one house, solution is to rob that
        if len(nums) == 1:
           return nums[0] 
        
        def maxRob(houses):
            #use the next house and next next house to compute max rob amount
            #base case -> next house = len - 1, next next = past all hgouses
            nextMaxRob, nextNextMaxRob =  houses[-1], 0            
            
            for i in range(len(houses) - 2, -1, -1):
                tmp = nextMaxRob
                nextMaxRob = max( houses[i] + nextNextMaxRob, nextMaxRob)
                nextNextMaxRob = tmp

            return nextMaxRob

        #return the max rob amount by compairng skiping the first house or the last
        return max( maxRob(nums[1:]),  maxRob(nums[:-1]) )


             