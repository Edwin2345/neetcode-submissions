class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy solution: treat last index as target, then check if reachable from second last index
        #if so, 2nd last index become target (now we can check if we can reach this locally optimal solutioon insttead), 
        #keep on decendign down array, updatign target, if target == 0 (first index) then tis possible

        target = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            #check if we can reach target from this distance, if so we have a new locally optimal target
            if i + nums[i] >= target:
               target = i             

        return True if target == 0 else False