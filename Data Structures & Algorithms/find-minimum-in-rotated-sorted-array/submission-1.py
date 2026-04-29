class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        rotating a sorted array contains 2 sorted portions
        [6,7,4,5]
        [4,5,1,2,3]

        mid in LSP -> if mid >= L
          if R < mid ->  L = mid+1 -> search RSP for smaller
          if R => mid ->  R = mid -> r must be at least there to BS min
        
        mid in RSP -> if mid < L
           -> must be min
        '''

        L=0
        R=len(nums)-1
        while(L < R):
            mid = L + (R-L)//2
            #mid in Right sorted portion
            if nums[mid] < nums[L]:
                #mid is less than R -> bring R down here
                if nums[R] < nums[mid]:
                   L = mid+1
                else:                    
                   R = mid
            #mid in Left sorted portion
            else:
                #mid is less than R -> search RSP
                if nums[R] < nums[mid]:
                   L = mid+1
                #otherwise, R has to atleast be here
                else:
                   R = mid 
                               
        #converge at the min value
        return nums[L]
