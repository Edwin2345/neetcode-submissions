class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums) - 1
  
        while L <= R:
            #compute midpoint and see if target there
            M = L + (R-L) // 2
            if nums[M] == target:
               return M
            
            #in RSP
            if nums[M] < nums[R]:
               #target belong in rsp, continue searching it
               if nums[M] < target <= nums[R]:
                  L = M + 1
               # target actually in LSP, go to that half
               else:
                  R = M - 1
            #in LSP
            else:
               #target in LSP, continue searching it
               if nums[L] <= target < nums[M]:
                  R = M - 1
               #otherwise go to RSP
               else:
                  L = M + 1  
            
        #numebr nto found
        return -1
