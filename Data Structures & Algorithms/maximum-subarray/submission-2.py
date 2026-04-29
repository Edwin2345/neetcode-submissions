class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        left = 0
        curSum = nums[0]
        '''
        [2,-3,4,-2,2,1,-1,4]
        '''

        for right in range(1,len(nums)):
            #keep on expanding subarray if adding is better than restarting
            if curSum + nums[right] >= nums[right]:
                curSum += nums[right]
            else:
                #restart subarray
                left = right
                curSum = nums[right]
            
            #update max sum
            maxSum = max(curSum, maxSum)

        return maxSum