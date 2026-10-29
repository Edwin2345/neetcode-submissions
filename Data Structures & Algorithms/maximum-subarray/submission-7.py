class Solution:
    #one way to look at it --> is it better to add current num to subarray or restart
    #at least one number
    def maxSubArray(self, nums: List[int]) -> int:
        #startung point for max sum
        maxSum = nums[0]
        
        #slidign window
        L, curSum = 0, 0
        maxL, maxR = 0, 0
        for R in range(len(nums)):
            #better to restart window here
            if curSum + nums[R] < nums[R]:
               L = R
               curSum = nums[R]
            #otherwise, add the num to the current subarray
            else:
               curSum += nums[R]  
            
            #update max sum
            maxSum = max(maxSum, curSum)
            maxL, maxR = L, R

        print("maximum subarray: ")
        print(nums[maxL : maxR + 1])
        return maxSum
        