class Solution:
    # rotated sorted -> produces two sorted portions LSP, RSP
    # if target belongs, continue to search in that, else go to the other sorted posrion
    # all nums are unique
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums) - 1

        while L <= R:
            M = L + (R - L) // 2

            #found target
            if nums[M] == target:
               return M

            # M is in RSP
            if nums[M] < nums[R]:
               #target is here, continue searching RSP
               if nums[M] < target <= nums[R]:
                  L = M + 1
               #otherwise go to LSP
               else:
                  R = M - 1
            #M isin LSP
            else:
                #target here, search LSP
                if nums[L] <= target < nums[M]:
                   R = M - 1
                #otherwise got to RSP
                else:
                   L = M + 1
        
        return -1
        
        