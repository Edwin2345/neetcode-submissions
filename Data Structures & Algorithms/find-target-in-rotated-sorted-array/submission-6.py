class Solution:
    #P: 2 sorted halfs, check if target is int he sorted ahlf or the other
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L <= R:
            #compute and check midpoint
            M = L + (R-L)//2
            if nums[M] == target:
               return M

            #LSH
            if nums[L] <= nums[M]:
               #target in this half, continue search   
               if nums[L] <= target < nums[M]:
                  R = M-1
               #else go RSH  
               else:
                  L = M+1
            #RSH
            else:
                #target in this half
                if nums[M] < target <= nums[R]:
                   L = M+1 
                #else go to LSH
                else:
                   R = M-1 
                       
        return -1
        