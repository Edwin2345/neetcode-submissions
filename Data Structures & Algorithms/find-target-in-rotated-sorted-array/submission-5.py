class Solution:
    #P: a rotated sorted array has LSH and RSH
    #P: L,R,M -> check if m is target
    #P: if in LSH arr[L] < arr[M], else RSH
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L <= R:
            #find midpoint and check if at target
            M = L + (R-L)//2
            if nums[M] == target:
               return M

            #LSH
            if nums[L] <= nums[M]:
               #we are in the correct half
               if nums[L] <= target < nums[M]:
                  R = M-1
               #otherwise, go the RSH
               else:
                  L = M+1                  
            #RSH
            else:
                #we are in the correct half
                if nums[M] < target <= nums[R]:
                   L = M+1
                #else, go to LSH
                else:
                   R = M-1
        
        return -1
