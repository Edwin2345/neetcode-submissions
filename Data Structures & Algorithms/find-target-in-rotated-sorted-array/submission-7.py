class Solution:
   #rotated sorted creates two sorted halfs LSH and RSH
   #we are LSH if nums[L] <= nums[mid], else RSH
   #do a binary search, but if we are not in correct half, go to other
   def search(self, nums: List[int], target: int) -> int:
       L = 0
       R = len(nums) - 1

       while L <= R:
         #compute mid index and check if its target
         mid = L + (R - L)//2
         if nums[mid] == target:
            return mid

         #LSH
         if nums[L] <= nums[mid]:
            #we are in correct half     
            if nums[L] <= target < nums[mid]:
               R = mid - 1
            #otherwise, go to RSH
            else:
               L = mid + 1          
         #RSH
         else:
            #we are in correct half
            if nums[mid] < target <= nums[R]:
               L =  mid + 1
            #otherwise go to LST
            else:
               R = mid -1

       return -1
        