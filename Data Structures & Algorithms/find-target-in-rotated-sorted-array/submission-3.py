class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two sorted portions, elft and right
        # [3,4,5,6,1,2]
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

            #mid is in right sorted portion
            if nums[mid] < nums[R]:
               #target belong sin the right sorted porution, continue to search higher
               if nums[mid] < target <= nums[R]:
                  L = mid+1
               #otherwise, search lef tportion
               else:
                  R = mid-1
            #mid is in left sorted portion
            else:
                #targe is in thsi portion
                if nums[L] <= target < nums[mid]:
                   R = mid-1
                #othersie, search right portion
                else:
                   L = mid+1  
            
        return -1