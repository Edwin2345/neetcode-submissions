class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        rotating a sorted array contains 2 sorted portions
        [6,7,4,5]
        [4,5,1,2,3]

        mid in LSP -> if mid >= L
          if R < mid ->  L = mid+1 -> search on right side
          if R => mid ->  R = mid -> r must be at least there to BS min
        
        mid in RSP -> if mid < L
          if R < mid ->  L = mid+1 -> search on right side
          if R => mid ->  R = mid -> r must be at least there to BS min
        '''

        L=0
        R=len(nums)-1
        while(L < R):
            mid = L + (R-L)//2
            # R must at least be at mid if lte
            if nums[mid] <= nums[R]:
                R = mid
            #right side is greater -> search the right side
            else:
                L = mid+1           
                               
        #converge at the min value
        return nums[L]
