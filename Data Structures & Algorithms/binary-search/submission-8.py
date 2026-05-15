class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(L,R):
            #not found
            if R < L:
               return -1

            mid = L + (R-L)//2            
            if nums[mid] == target:
               return mid
            elif nums[mid] > target:
               return binarySearch(L, mid-1)
            else:
               return binarySearch(mid+1, R)    
        
        return binarySearch(0,len(nums)-1)