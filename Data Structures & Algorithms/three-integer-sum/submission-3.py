class Solution:
    #O(n^3) solution, use 3 indices and a set to get all unique answers
    #sort the nums so that duplicates get filterd (unique combos only)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSumVals = []
        
        nums.sort()

        for firstIndx , num in enumerate(nums):
            #skip duplicates
            if firstIndx > 0 and nums[firstIndx] == nums[firstIndx - 1]:
               continue

            #search for remaining 2 numbers with two pointer appr
            L = firstIndx + 1
            R = len(nums) - 1
            while L < R:
                  threeSum = nums[firstIndx] + nums[L] + nums[R]  
                  #foudn valid solution
                  if threeSum == 0:
                      #add valid pair to result set
                      threeSumVals.append( [nums[firstIndx], nums[L], nums[R]] )
                      
                      #move to next to two number combo, skiping duplicates
                      L += 1
                      while L < R and nums[L] == nums[L-1]:
                        L += 1
                      R -= 1
                      while L < R and nums[R] == nums[R+1]:
                        R -= 1
                  #sum is too large, shrink by moving left
                  elif threeSum > 0:
                     R -= 1
                  #sum is too small, move right
                  else:
                     L += 1
        
        return threeSumVals