class Solution:
    def findMin(self, nums: List[int]) -> int:
        #minimun is located in left most side of the right sorted poriton
        L, R = 0, len(nums)-1
        while L < R:
            M = L + (R-L)//2
            # in right sorted portion -> keep tryign to shift left
            if nums[M] <= nums[R]:
               R = M
            #in left sorted portion -> shift to right sorted portion
            else:
               L = M + 1 

        return nums[L]