class Solution:
    #straight line --> once we reach end we are done
    def rob(self, nums: List[int]) -> int:

        #bottom up dynamic programming
        #need i+1 and i+2 states to compute max rob at ith
        #base case at i == len(nums) -> max rob is 0, at last index max rob is whatever
        dp = [nums[-1],0]
        for i in range(len(nums)-2, -1, -1):
            #store i+1 state and compute max rob at current index
            tmp = dp[0]
            dp[0] = max(nums[i] + dp[1], dp[0])
            # store i+1 state at i+2 for next iteration
            dp[1] = tmp

        return dp[0]
        