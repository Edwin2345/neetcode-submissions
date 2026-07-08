class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(L,R):
            #base case: item not found
            if L > R:
               return -1               
            #check current index
            mid = L + (R-L)//2
            if nums[mid] == target:
               return mid
            #otehrwise search hgiehr or lower as approiate
            elif nums[mid] > target:
               return binarySearch(L,mid-1)
            else:
               return binarySearch(mid+1,R)
         
        return binarySearch(0, len(nums)-1)
            