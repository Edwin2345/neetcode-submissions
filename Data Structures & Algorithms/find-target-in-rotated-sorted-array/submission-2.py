class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two sorted portions, elft and right
        #check which one mid is in
        # if target belongs int hat sorted post continue tos earch threre
        # else go to other poriton
        
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = L + (R-L)//2
            
            #found target
            if nums[mid] == target:
               return mid

            #mid is in left sorted portion
            if nums[L] <= nums[mid]:
               #target should be in this portion, search lower
               if nums[L] <= target < nums[mid]:
                  R = mid-1
               #iotherwise target is in right sorted poriton
               else:
                  L = mid+1
            #mid is in right sorted potion
            else:
                #target should be in this portion, search higher
                if nums[mid] < target <= nums[R]:
                   L = mid + 1
                #otherwise, search left sorted portion
                else:
                   R = mid-1       
            
        return -1