class Solution:
    #P: Rotated sorted causes there to be LSP and RSP
    #P: minimun occurs where the RSP begins
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1

        while L < R:
            mid = L + (R-L)//2
            #we are in RSP -> try to go left to get to start of RSP
            if nums[mid] <= nums[R]:            
               R = mid
            #we are in LSP -> shift right to try tog et to rsp
            else:
               L = mid + 1 

        return nums[L]


        