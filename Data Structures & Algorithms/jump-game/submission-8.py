class Solution:
   # dynamic programming: bottom up
    def canJump(self, nums: List[int]) -> bool:
        #start at goal = last index
        #iterate through nums in reverse order and see if we cna reach goal from there
        #if at the end goal is 0 -> then we cna jump to top
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            #able to jump to target, shift target
            if i + nums[i] >= goal:
               goal = i 

        return (goal == 0)
        