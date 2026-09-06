class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while L <= R:
            #calc midpoitn and check if you found target
            M = L + (R - L) // 2
            if nums[M] == target:
               return M
            
            #in left sorted poriton
            if nums[L] <= nums[M]:
               #target belongs to this sorted position -> continue search
               if nums[L] <= target < nums[M]:
                  R = M-1
               #otherwise, move to the right sorted portion -> past midpoint
               else:
                  L = M+1
            #in right sorted potion
            else:
               #target belongs to this sorted position -> continue search 
               if nums[M] < target <= nums[R]:
                  L = M+1
               #otheriwse go to left sorted portion
               else:
                  R = M-1
         
        #not found
        return -1
