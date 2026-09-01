class Solution:
    #Question: subarray can't be empty right?
    #optimal greedy: at each index make local decision -> is it better to retstart subarry or add to subarry
    #better to restart at this index if its valeu is greater than what it would be if we added it
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        sm = 0
        for i in range(len(nums)):
            if sm + nums[i] < nums[i]:
               sm = nums[i] 
            else:
               sm += nums[i]
            
            maxSum = max(maxSum, sm)

        return maxSum
        