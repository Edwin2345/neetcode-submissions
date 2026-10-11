class Solution:
    def rob(self, nums: List[int]) -> int:
        #edeg case, onyl 1 houses
        if len(nums) == 1:
           return nums[0] 
        
        def calcMaxRob(houses):
            #store the max rob amount at house i+1 and i+2 in dp[0] and dp[1] resp
            #base case, past last house max rob is 0, at last hosue max rob is that hosue

            dp = [houses[-1], 0]
            for i in range(len(houses)-2, -1, -1):
                tmp = dp[0]
                #calcualte the max rob based on 2 options (rob current and go i+2, or skip to i+1)
                dp[0] = max(houses[i] + dp[1], dp[0])
                #assign i+1 to i+2 state
                dp[1] = tmp
            
            return dp[0]
            

        return max(
            calcMaxRob(nums[1:]),
            calcMaxRob(nums[:len(nums)-1])
        )