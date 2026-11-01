class Solution:
    #TC: O(N), SC: O(1)
    def canJump(self, nums: List[int]) -> bool:
        #bottom up dynamic programing - work backwrds form the goal (last index)
        minReachableIndex = len(nums)- 1
        for i in range(len(nums) - 2, -1, -1):
            #if from i you can reach minReachable, that becomes new minRechable
            if i + nums[i] >= minReachableIndex:
               minReachableIndex = i    

        #can only return true if can reach end from index 0
        return minReachableIndex == 0

        