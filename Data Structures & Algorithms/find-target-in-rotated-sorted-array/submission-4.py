class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search, but you ahve 2 sorted halves
        L=0
        R=len(nums)-1

        while L <= R:
           #compute mid and see if it matches target
           mid = L + (R-L)//2
           if nums[mid] == target:
              return mid

           #we are in the right sorted half
           if nums[mid] < nums[R]:
              #target is in right sorted half
              if nums[mid] < target <= nums[R]:
                 L = mid + 1
              else:
                 R =  mid - 1
           #we are in left sorted half   
           else:
               #target is here
               if nums[L] <= target < nums[mid]:
                  R = mid - 1
               else:
                  L = mid + 1
        
        return -1
              