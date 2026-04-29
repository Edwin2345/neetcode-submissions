class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        L = 0
        
        for R in range(len(nums)):
            # if adding less than current -> better to restart 
            if currSum + nums[R] < nums[R] :
                currSum = nums[R]
                L = R
            #otherwise keep on adding
            else:
                currSum += nums[R]
               
            #Global Check
            maxSum = max(maxSum, currSum)


        return maxSum