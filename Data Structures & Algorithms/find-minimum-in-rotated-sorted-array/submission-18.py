class Solution:
    #rotated sorted, gives two sorted halves --> min occurs at the begiingin of the right sorted portion
    #unique nums only
    #O(logN) TC, O(1) SC
    def findMin(self, nums: List[int]) -> int:
        L,R = 0, len(nums) - 1
        
        while L < R:
            M = L + (R-L) // 2

            #in the right sorted portion already, try to go to the beigin of this seciton
            if nums[M] < nums[R]:
               R = M
            #in the left sorted portion, need to go to right side
            else:
               L = M + 1 
            
        
        #point where they converge is the minimum
        return nums[L]
        