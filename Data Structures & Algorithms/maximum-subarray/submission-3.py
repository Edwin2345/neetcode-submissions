class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #greedy approach -> for each val, if adding it to sum is larger than the val itself, take it
        #otherwise, we decide to restart subaray there, take global max value of subArray
        maxVal = nums[0]
        currSum = 0
        maxCoord = [0,0]
        L = 0
        R = 0
        for i in range(len(nums)):
            if currSum + nums[i] > nums[i]:
               currSum += nums[i]
               R = i
            else:
               currSum = nums[i]  
               L = i            
            
            if maxVal < currSum:
               maxVal = currSum
               maxCoord[0] = L
               maxCoord[1] = R

        print(f"Maximum Subarray from index {maxCoord[0]} to index {maxCoord[1]}")
        return maxVal
            
