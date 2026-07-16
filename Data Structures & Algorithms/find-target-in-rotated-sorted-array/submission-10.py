class Solution:
   #rotated sorted creates two sorted poritons LSP and RSP
   #EVERY element in LSP is greate than RSP
   #we are RSP if nums[mid] < nums[R], else RSP
   #do a binary search, but if we are not in correct portion, go to other
   def search(self, nums: List[int], target: int) -> int:
       L = 0
       R = len(nums) - 1

       while L <= R:
         #compute mid index and check if its target
         mid = L + (R - L)//2
         if nums[mid] == target:
            return mid

         #RSP
         if nums[mid] < nums[R]:
            #in correct portiton
            if nums[mid] < target <= nums[R]:
               L = mid + 1
            #otherwise move to left
            else:
               R = mid - 1
         #LSP
         else:
            #in correct portion
            if nums[L] <= target < nums[mid]:
               R = mid - 1
            #otherwise move to right
            else:
               L = mid + 1

       return -1
        