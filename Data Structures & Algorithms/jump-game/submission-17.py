class Solution:
    # at least one num and values are non-neg
    # bottom up DP, work bakcwads from end, if an index can reach end by jumping, that is new target
    # TC: O(N) 
    # SC: O(1)
    def canJump(self, nums: List[int]) -> bool:
        targetIndex = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= targetIndex:
               targetIndex = i 
        
        return targetIndex == 0
