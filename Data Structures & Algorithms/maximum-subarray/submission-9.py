class Solution:
    #at least 1 num
    #optimizaiton form brute force: if adding the curNum to sum makes it smaller than restarting -> restart
    #can do this in one pass
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], nums[0]
        L = 0
        for R in range(1,len(nums)):
            if curSum + nums[R] < nums[R]:
               curSum = nums[R]
               L = R
            else:
               curSum += nums[R]

            maxSum = max(maxSum, curSum) 

        return maxSum
        