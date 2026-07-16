class Solution:
   #rotated sorted creates two sorted poritons LSP and RSP
   #we are LSP if nums[L] <= nums[mid], else RSP
   #do a binary search, but if we are not in correct portion, go to other
   def search(self, nums: List[int], target: int) -> int:
       L = 0
       R = len(nums) - 1

       while L <= R:
         #compute mid index and check if its target
         mid = L + (R - L)//2
         if nums[mid] == target:
            return mid

         #LSP
         if nums[L] <= nums[mid]:
            #we are in correct portion     
            if nums[L] <= target < nums[mid]:
               R = mid - 1
            #otherwise, go right
            else:
               L = mid + 1          
         #RSP
         else:
            #we are in correct portion
            if nums[mid] < target <= nums[R]:
               L =  mid + 1
            #otherwise go left
            else:
               R = mid -1

       return -1
        