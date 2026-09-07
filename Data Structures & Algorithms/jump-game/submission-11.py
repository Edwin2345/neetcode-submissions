class Solution:
    #1dp dp botom up -> we use the previous states fo being already at top and see if reachbale from prev states
    def canJump(self, nums: List[int]) -> bool:

        targetIndex = len(nums) - 1
        for i in range(targetIndex - 1 , -1, -1):
            #can reach target from this index -> if so shift oru target to here
            if i + nums[i] >= targetIndex:
               targetIndex = i 

        return (targetIndex == 0)
        